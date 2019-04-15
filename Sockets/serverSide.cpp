/**
 * @file    serverSide.cpp
 * @brief   Implementação de arquitetura cliente-servidor no lado do servidor
 */

#include <iostream>
#include <string>

/// BIBLIOTECAS P/ SOCKETS
#include <arpa/inet.h>
#include <netinet/in.h>  /// AF_INET
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>

#define PORT_NUMBER 4325
#define QUEUE_SIZE_OF_REQUISITIONS 10

int main(){
   
    struct sockaddr_in addrServer;
    addrServer.sin_addr.s_addr = inet_addr("127.0.0.1");
    addrServer.sin_port = htons( PORT_NUMBER );
    addrServer.sin_family = AF_INET;

    /// CRIANDO O SOCKET IPV4 DO SERVIDOR
    int socketId_Server = socket(AF_INET, SOCK_STREAM, NULL);
    
    if( socketId_Server != 0){
        std::cerr << "Falha ao executar o socket do Servidor..." << std::endl;
        exit(EXIT_FAILURE);
    }

    std::cout << "Socket Servidor criado com sucesso..." << std::endl;

    /// LIGANDO O SOCKET CRIADO DO SERVIDOR À PORTA PORT_NUMBER
    if( bind( socketId_Server,
              (struct sockaddr*) &addrServer,
              sizeof(addrServer)   
            ) != 0 ){
        std::cerr << "Falha em ligar o socket do Servidor a porta " + PORT_NUMBER << (std::string)"..." << std::endl;
        exit(EXIT_FAILURE);                
    }

    std::cout << "A ligacao do socket do Servidor a porta " + PORT_NUMBER + (std::string)" foi um sucesso..." << std::endl;

    /// HABILITA O SOCKET DO SERVIDOR A ESCUTAR REQUISIÇÕES 
    if( listen( socketId_Server, 
                QUEUE_SIZE_OF_REQUISITIONS
               ) != 0){
        std::cerr << "Falha em fazer o socket do Servidor escutar requisicoes..." << std::endl;
        exit(EXIT_FAILURE);                           
    }

    std::cout << "O socket do Servidor esta ouvindo se ha requisicoes..." << std::endl;

    /// RETIRANDO REQUISIÇÃO PENDENTE DA CABEÇA DA FILA DE REQUISIÇÕES
    struct sockaddr_in addrCliente;   
    socklen_t cliente_len = sizeof(addrCliente);

    int socketId_Client_Conexao = accept( socketId_Server,
                                (struct sockaddr*)& addrCliente,
                                &cliente_len);

    std::cout << "Socket do Servidor recebeu conexao de " << inet_ntoa(addrCliente.sin_addr) << std::endl;

    if( socketId_Client_Conexao != 0 ){
        std::cerr << "Falha ao retira requisicao da frente da fila de requisicoes..." << std::endl;
        exit(EXIT_FAILURE);
    }    
    
    std::cout << "Requisicao retirada da frente da fila de requisicoes com sucesso..." << std::endl;
        
    /// ENVIANDO MENSAGEM DO SOCKET DO SERVIDOR PARA O SOCKET DO CLIENTE 
    std::string mensagemDoServidor("Oi oi oi....\nTestando...\n");

    if ( send( socketId_Client_Conexao, 
               mensagemDoServidor.c_str(), 
               mensagemDoServidor.size(), 0 
            ) != 0 ){
        std::cerr << "Falha no envio da mensagem por parte do socket do Servidor..." << std::endl;
        exit(EXIT_FAILURE);                           
    }

    std::cout << "O socket do Servidor enviou a seguinte mensagem: " << mensagemDoServidor << std::endl;
    
    //// QUEBRANDO CONEXÃO ENTRE O SOCKET DO SERVIDOR E O DO CLIENTE
    close(socketId_Client_Conexao);
    close(socketId_Server);

    std::cout << "Conexao entre os sockets do Servidor e do Cliente foi quebrada..." << std::endl;
    

    return EXIT_SUCCESS;
}    