/**
 * @file  part2.cpp
 * @brief Contém as impressões periódicas na tela e a criação do JSON
 */
#include <cstdlib>
#include <cstdio>
#include <fstream>
#include <string>
#include <cerrno>

/// BIBLIOTECAS DO UNIX/LINUX
#include <sys/select.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include "tree.cpp"

#define NMAX 80

using namespace std;

/**
 * @brief       Salva a arvore de hierarquia no fomato JSON 
 * @param json  String com conteúdo de arquivo JSON        
 * @param pid   Número de identificação do processo
 */
void saveFile(string jsonTree, int pid){
    string file = "json/" + to_string(pid) + ".json";
    ofstream out(file.c_str());
    out << jsonTree;
    out.close();
    printf("TREE GENERATED WITH SUCCESS ON %s\n", file.c_str());
}

int main() {
    // https://linux.die.net/man/3/fd_set
    fd_set rfds;
    struct timeval tv;
    char buf[NMAX];
    int nRead, num_bytes, fd_stdin;
    printf("Hello, welcome to the hierarchy of processes, to get hierarchy tree relative some process, just enter the PID of the desired process at any time.\nIn addition, if you want to get the total number of processes in the system and the total number of processes per system user, simply do not enter anything that periodically the program will print this information on the screen!!!!\n");

    tv.tv_sec = 12;
    tv.tv_usec = 0;
    while(1) {
        fd_stdin = fileno(stdin);
        FD_ZERO(&rfds);
        FD_SET(fileno(stdin), &rfds);
        printf("Enter some PID(Press 0 to stop): ");
        fflush(stdout);
        nRead = select(fd_stdin + 1, &rfds, NULL, NULL, &tv);

        if ( nRead==-1 ) 
        {
            fprintf(stderr, "\nError reading!\n");
            exit(1);
        }
        if ( nRead==0 ) 
        {
            system("clear");
            printf("Number of processes in the system: ");
            fflush(stdout);
            /// Sinc
            system("ps aux|wc -l ");
            printf("\n");
            printf("Number of processes in the system per user:\n");
            fflush(stdout);
            /// Sinc
            system("ps -eo user=|sort|uniq -c ");
            printf("\n");
            tv.tv_sec += 8;
        } 
        else 
        {
            num_bytes = read(fd_stdin, buf, NMAX);
            if ( num_bytes < 0 )
            {
                fprintf(stderr, "\nError on read : %s\n", strerror(errno));
                exit(1);
            }
            if( atoi(buf) == 0 ) break;
            if( pidChack(atoi(buf))) saveFile( getJsonTree(atoi(buf)), atoi(buf) );
            else printf("PID:%d é invalid\n", atoi(buf));
        }
    }
    return 0;
}