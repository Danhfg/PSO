#include <iostream>

/// BIBLIOTECAS P/ SOCKETS
#include <arpa/inet.h>
#include <netinet/in.h>  /// AF_INET

#define HOST "127.0.0.1"
#define PORT_NUMBER 4325
#define MESSAGE_SIZE 40 /// Quantidade de caracteres que uma mensagem pode transmitir  

int main(){ 

    /// CONFIGURANDO AS PROPRIEDADES DA CONEXAO
    struct sockaddr_in addrServer;
    addrServer.sin_addr.s_addr = inet_addr( HOST );
    addrServer.sin_port = htons( PORT_NUMBER );
    addrServer.sin_family = AF_INET;

    /// CRIANDO O SOCKET (AF_INET = IPV4) DO CLIENTE
    int socketId_Cliente = socket(AF_INET, SOCK_STREAM, NULL);

    if( socketId_Cliente != 0){
        std::cerr << "Falha ao executar o socket do Cliente..." << std::endl;
        exit(EXIT_FAILURE);
    }

    std::cout << "Socket do Cliente criado com sucesso..." << std::endl;

    /// ESTABELECENDO CONEXÃO VIA SOCKETS ENTRE O **CLIENTE** E O SERVIDOR
    if( connect( socketId_Cliente, 
                 (struct sockaddr *) &addrServer, 
                  sizeof(addrServer) 
                ) != 0 ){
        std::cerr << "Falha ao conectar o socket do Cliente e o do Servidor..." << std::endl;
        exit(EXIT_FAILURE);
    }

    std::cout << "Cliente conectado ao Servidor (via sockets)..." << std::endl;

    char bufferServer[MESSAGE_SIZE];

    /// SOCKET DO CLIENTE RECEBENDO MENSAGEM DO SOCKET DO SERVIDOR
    int messageSizeReceived = recv(socketId_Cliente, bufferServer, MESSAGE_SIZE, 0);

    if( messageSizeReceived > 0 ){ /// Situação em que o Servidor mandou uma mensagem não vazia
        std::cout << "Servidor disse: " 
             << bufferServer 
             << ". Logo, o servidor esta conectado..."
             << std::endl;
    }

    while( true ){

        std::cin >>     

        if( messageSizeReceived > 0 ){  /// Situação em que o cliente mandou uma mensagem não vazia
            std::cout << "Servidor disse: " << bufferServer_temporaly << std::endl;
        }

        std::string serverResponse;
        std::getline(std::cin, serverResponse);

        send( socketId_Cliente, serverResponse.c_str(), MESSAGE_SIZE, 0 );



    }


    return EXIT_SUCCESS;

}    


