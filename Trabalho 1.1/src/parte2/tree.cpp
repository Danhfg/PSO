/**
 * @file  arvore.cpp
 * @brief Contém a implementação da árvore de processos além das funções auxiliares
 */ 

#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>

using namespace std;

/**
 * @brief   Verifica se o ppid passado é pai do processo pid passado
 * @param   ppid    Número de identificação do processo pai
 * @parama  pid     Número de identificação do processo
 */ 
bool parent(long ppid, long pid) 
{
    char pf[40], row[100], *idAux;

    FILE* readStatus;
    snprintf(pf, 40, "/proc/%ld/status", pid);
    readStatus = fopen(pf, "r");
    if(!readStatus) return false;
    // Busca pelo id do pai
    while(fgets(row, 100, readStatus)) 
    {
        if(strncmp(row, "PPid:", 5) != 0) continue;
        idAux = row + 5;
        while(isspace(*idAux)) ++idAux;
        break;  
    }
    fclose(readStatus);

    // Comparação entre o ppid passado por parâmetro com o ppid encontrado
    if(ppid == atoi(idAux)) return true;
    else return false;
}

/**
 * @brief   Checka a existencia de um pid no sistema
 * @param   pid Número de identificação do processo
 * @return  True caso exista; caso contrário, false
 */
bool pidChack(long pid)
{
    char pf[40], row[100], *idAux;
    FILE* readStatus;

    snprintf(pf, 40, "/proc/%ld/status", pid);
    readStatus = fopen(pf, "r");
    if(!readStatus) return false;
    // Busca pelo id do pai
    while(fgets(row, 100, readStatus)) {
        if(strncmp(row, "Pid:", 4) != 0) continue;
        idAux = row + 4;
        while(isspace(*idAux)) ++idAux;
        break;
    }
    fclose(readStatus);

    // Comparação entre o pid passado por parâmetro com o pid encontrado
    if(pid == atoi(idAux)) return true;
    else return false;
}

/**
 * @brief   Lista o pid de todos os processos em execução no sistema
 * @return  Uma lista com todos os processos em execução no sistema
 */ 
list<int> listOfProcess(){
    FILE *filec;
    char pf[1035];
    list <int> process;

    string comando = "ls /proc | grep '^[0-9]'";
    filec = popen(comando.c_str(), "r");
    if (filec == nullptr) 
    {
        printf("Could not open file!!!!!\n" );
        exit(1);
    }
    while (fgets(pf, sizeof(pf)-1, filec) != nullptr) 
    {
        process.push_back(atoi(pf));
    }
    pclose(filec);

    return process;
}

/**
 * @brief   Gera a árvore de de hierarquia filhos e coloca numa string formatada
 * @return  O JSON da árvore de processos de um determinado Pid
 */ 
string getJsonTree(long pid)
{
    string jsonTree = "{ PID: " + to_string(pid) + ", CHILDREN: [";
    list<int> process = listOfProcess();

    for(list<int>::iterator it = process.begin(); it != process.end(); ++it)
    {
        if(parent(pid,*it) == true){
            if (jsonTree.back() != '[') jsonTree += ",";
            jsonTree += getJsonTree(*it);
        }
    }
    jsonTree += " ] }";

    return jsonTree;
}