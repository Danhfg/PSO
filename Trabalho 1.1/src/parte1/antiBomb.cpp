/**
 * @file  antiBomb.cpp
 * @brief Contém a implementação de um anti fork bomba
 */ 

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <cstdlib>
#include <cstring>

#include <unistd.h> /// fork()

using namespace std;

int main() {
    std::ifstream processLog;
    std::map <std::string, std::string> mapPid;
    std::map <std::string, int> mapCounter;
    int processLimit = 0;
    std::cout << "set the number of processes supported by the program: ";
    std::cin >> processLimit;
    std::cout << "List of dead process: " << std::endl;

    while (1) {
        /** ps -ec é o comando linux que lista todas as informações do 
          * agendador de processos. Além disso, awk o comando é para 
          * manipular arquivos de texto formatados de maneira previsível, 
          * no nosso caso, utilizamos para selecionar as colunas 1(PID)
          * e 6(CMD) e pular o cabeçalho (if (NR!=1)).
          */
        std::system("ps -e |awk '{if (NR!=1) print $1,$4 }'> process.log");
        processLog.open("process.log");

        if (processLog.is_open()) {
            std::string processName, pid;
            // Lê a primeira string e carrega para a variável pid.
            while (processLog >> pid) {
                // Lê a segunda string e carrega para a variável processName.
                processLog >> processName;
                // Salva as strings nos mapas.
                ++mapCounter[processName];
                mapPid[pid] = processName;
            }
            processLog.close();
            // Faz uma varredura para encontrar algum nome com muitos processos associados
            /** Com a lista de processos lida, o próximo passo é encontrar programas que
             *  possívelmente seja um forkbomb.
             */
            for (std::map<std::string, int>::iterator iter = mapCounter.begin();
                 iter != mapCounter.end(); ++iter) 
            {
                // Verifica se o processo está no limite. Caso não esteja ele será eliminado.
                if(iter->second > processLimit) {
                    bool starting = 1;
                    int pidPai, aux;
                    // Procura o processo pai para eliminar.
                    for (std::map<std::string, std::string>::iterator iter2 = mapPid.begin();
                         iter2 != mapPid.end(); ++iter2) 
                    {
                        if (iter->first.compare(iter2->second) == 0) 
                        {
                            if (starting) 
                            {
                                pidPai = std::stoi(iter2->first);
                                starting = false;
                            }
                            else 
                            {
                                aux = std::stoi(iter2->first);
                                if (pidPai > aux && aux > 1) 
                                {
                                    pidPai = aux;
                                }
                            }
                        }
                    }
                    /** Matar a árvore de processos relacionada ao pidPai   
                      * http://fibrevillage.com/sysadmin/237-ways-to-kill-parent-and-child-processes-in-one-command                         
                      */
                    std::string ps = "ps -eo ppid | grep -w " + std::to_string(pidPai)+
                                     " | wc -w > num_proc.temp";
                    std::system(ps.c_str());
                    std::ifstream num_proc;
                    num_proc.open("num_proc.temp");
                    std::string num;
                    getline(num_proc, num);
                    num_proc.close();
                    std::string killProcessTree = "kill -9 -$(ps -o pgid= " +
                                              std::to_string(pidPai) + " | grep -o '[0-9]*')";
                    std::system(killProcessTree.c_str());
                    std::cout <<"PID: " << pidPai << ";name: " << mapPid[std::to_string(pidPai)] 
                              << "; number of children:"<< std::to_string(iter->second) <<std::endl;
                    usleep(1000000);
                }
            }
            mapCounter.clear();
            mapPid.clear();
        }
        else {
            std::cout << "Could not open file!!!!! ";
            exit(-1);
        }
	usleep(1000000);
    }

    return 0; 
}
