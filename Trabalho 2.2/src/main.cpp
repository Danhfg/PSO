/**
 * @file  main.cpp
 */
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void imprimeDadosDaMemoria();

int main() {
    
    struct timeval tv;
    
    printf("Hello, welcome to the process manager.\nIn addition, if you want to get the total number of processes in the system and the total number of processes per system user, simply do not enter anything so that the program periodically prints this information on the system. screen !!!! \n");

    tv.tv_sec = 12;
    tv.tv_usec = 0;
    
    while(true) {
        system("cat /proc/meminfo > memInfo.dat");
        system("clear");

        imprimeDadosDaMemoria();      
            
        tv.tv_sec += 8;
        
    }

    return 0;
}

void imprimeDadosDaMemoria(){

    ifstream arqMemInfo("memInfo.dat");
    string conteudoArqMemInfo;

    system("grep 'MemTotal' memInfo.dat > memTotal.dat");
    system("grep 'Cached' memInfo.dat > cacheTotal.dat");
    system("grep 'Cached' memInfo.dat > cacheTotal.dat");


    // if( arqMemInfo.is_open() ){
    //     while( arqMemInfo >> conteudoArqMemInfo );
    //     cout << conteudoArqMemInfo


    //     cout << ""
    // }
}