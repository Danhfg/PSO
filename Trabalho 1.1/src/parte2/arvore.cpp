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
 * @brief   Verifica se o ppid é pai do processo pid
 * @param   ppid    Número de identificação do processo pai
 * @parama  pid     Número de identificação do processo
 */ 
bool isPai(long ppid, long pid) {

    /// Inicialização das variáveis
    char path[40], line[100], *p;
    FILE* statusf;

    /// Procura pelo arquivo status do processo procurado
    snprintf(path, 40, "/proc/%ld/status", pid);

    /// Abre o arquivo
    statusf = fopen(path, "r");

    /// É verificado se foi possível abrir o arquivo informado
    if(!statusf)
        return false;

    /// Leitura do arquivo linha por linha
    while(fgets(line, 100, statusf)) {
        
        /// Verifica se a linha é a linha que contém o PPid do processo
        if(strncmp(line, "PPid:", 5) != 0)
            continue;
        
        /// É tirado da string a parte 'PPid:' para ser verificado somente o número PPid em questão
        p = line + 5;

        /// Enquanto houver caracteres nulos, eles são retirados da string;
        while(isspace(*p)) ++p;

        break;  
    }

    /// Fechando o arquivo
    fclose(statusf);

    /// Verificando se o PPid passado como parâmetro é igual ao PPid achado no arquivo
    if(ppid == atoi(p))
        return true;
    else
        return false;
}

/**
 * @brief   Verifica se o pid é um processo que existe no sistema
 * @param   pid Número de identificação do processo
 * @return  True caso exista; caso contrário, false
 */
bool isValid(long pid) {

    /// Inicialização das variáveis
    char path[40], line[100], *p;
    FILE* statusf;

    /// Procura pelo arquivo status do processo procurado
    snprintf(path, 40, "/proc/%ld/status", pid);

    /// Abre o arquivo
    statusf = fopen(path, "r");

    /// É verificado se é possivel abrir o arquivo informado
    if(!statusf)
        return false;

    /// Leitura do arquivo linha por linha
    while(fgets(line, 100, statusf)) {

        /// Verifica se a linha é a linha que contém o PPid do processo
        if(strncmp(line, "Pid:", 4) != 0)
            continue;
        
        /// É tirado da string a parte 'Pid:' para ser verificado somente o PPid em questão
        p = line + 4;

        /// Enquanto houver caracteres nulos, eles são retirados da string;
        while(isspace(*p)) ++p;

        break;
    }

    /// Fecha o arquivo
    fclose(statusf);

    //Verfica se o Pid passado como parâmetro é igual ao Pid achado no arquivo
    if(pid == atoi(p))
        return true;
    else
        return false;
}

/**
 * @brief   Descobre o pid de todos os processos abertos no sistema
 * @return  Lista com todos os processos abertos no sistema
 */ 
list<int> getProcessosAbertos(){

    /// Inicialização das variáveis
    FILE *fp;
    char path[1035];
    list<int> processosAbertos;

    /// Comando linux que pega todos pid dos processos abertos ordenados pelo primeiro dígito 
    string comando = "ls /proc | grep '^[0-9]'";

    /// O comando é executado no terminal e a saída é armazenada em um arquivo
    fp = popen(comando.c_str(), "r");

    /// Verifica se o comando foi executado
    if (fp == NULL) {
        printf("Failed to run command\n" );
        exit(1);
    }

    /// Lendo a saída linha por linha
    while (fgets(path, sizeof(path)-1, fp) != NULL) {

        //Adiciona o pid em uma lista de processos abertos
        processosAbertos.push_back(atoi(path));
    }

    /// Fecha o arquivo
    pclose(fp);

    return processosAbertos;
}

/**
 * @brief   Descobre a árvore de processos filhos e coloca numa string formatada
 * @return  O JSON da árvore de processos de um determinado Pid
 */ 
string getArvore(long pid){

    /// Inicializa o JSON com o pid, e setando os filhos
    string json = "{ pid: " + to_string(pid) + ", filhos: [";

    /// Inicializando com a lista de processos abertos
    list<int> processosAbertos = getProcessosAbertos();

    /// Percorrendo a lista de processos abertos
    for(list<int>::iterator it = processosAbertos.begin(); it != processosAbertos.end(); ++it){

        /// Verificando se o pid é pai do processo atual
        if(isPai(pid,*it)){

            /// Verificando se a última linha do JSON é '[', para saber se é o primeiro elemento da lista de filhos
            if (json.back() != '[')
                json += ",";

            /// Adicionando ao json a árvore do filho 
            json += getArvore(*it);
        }
    }

    /// Fechando o JSON
    json += " ] }";

    return json;
}