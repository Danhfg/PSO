/**
 * @file    serverSide.cpp
 * @brief   Implementação de arquitetura cliente-servidor (TCP) no lado do servidor
 */

#include <iostream>
#include <string>

/// BIBLIOTECAS P/ SOCKETS
#include <arpa/inet.h>
#include <netinet/in.h>  /// AF_INET
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>

#define HOST "127.0.0.1"
#define PORT_NUMBER 4325    /// Numero da porta usada pelo socket do Servidor
#define QUEUE_SIZE_OF_REQUISITIONS 10   /// Tamanho da lista de requisicoes
#define MESSAGE_SIZE 40 /// Quantidade de caracteres que uma mensagem pode transmitir  

int main(){
   
    struct sockaddr_in addrServer;
    addrServer.sin_addr.s_addr = inet_addr( HOST );
    addrServer.sin_port = htons( PORT_NUMBER );
    addrServer.sin_family = AF_INET;

    /// CRIANDO O SOCKET IPV4 DO SERVIDOR COM PROTOCOLO TCP
    int socketId_Server = socket(AF_INET, SOCK_STREAM, NULL);
    
    if( socketId_Server != 0){
        std::cerr << "Falha ao criar o socket do Servidor..." << std::endl;
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
    std::string bufferServer("Oi oi oi....\nTestando...\n");

    if ( send( socketId_Client_Conexao, 
               bufferServer.c_str(), 
               MESSAGE_SIZE, 0 
            ) != 0 ){
        std::cerr << "Falha no envio da mensagem por parte do socket do Servidor..." << std::endl;
        exit(EXIT_FAILURE);                           
    }

    std::cout   << "O socket do Servidor enviou a mensagem " 
                << bufferServer 
                << ". Logo, o cliente esta conectado..."
                << std::endl;
    
    /// COMUNICANDO-SE COM O CLIENTE
    do{

        int messageSizeReceived = recv( socketId_Client_Conexao, 
                                        bufferServer,
                                        MESSAGE_SIZE, 0 )

        if( messageSizeReceived > 0 ){  /// Situação em que o cliente mandou uma mensagem não vazia
            std::cout << "Cliente disse: " << << std::endl;
        }

        std::string serverResponse;
        std::getline(cin, serverResponse);

        send( socketId_Client_Conexao, serverResponse.c_str(), MESSAGE_SIZE, 0 );

    }while( mensagemDoCliente != "tchau" ||
            mensagemDoCliente != "bye" || 
            mensagemDoCliente != "Ate logo")


    //// QUEBRANDO CONEXÃO ENTRE O SOCKET DO SERVIDOR E O DO CLIENTE
    close(socketId_Client_Conexao);
    close(socketId_Server);

    std::cout << "Conexao entre os sockets do Servidor e do Cliente foi quebrada..." << std::endl;
    

    return EXIT_SUCCESS;
}    