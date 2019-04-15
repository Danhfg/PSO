#include <iostream>

/// BIBLIOTECAS P/ SOCKETS
#include <arpa/inet.h>
#include <netinet/in.h>  /// AF_INET

#define PORT_NUMBER 4325

int main(){
  

    struct sockaddr_in addrClient;
    addrClient.sin_addr.s_addr = inet_addr("127.0.0.1");
    addrClient.sin_port = htons( PORT_NUMBER );
    addrClient.sin_family = AF_INET;


    /// CRIANDO O SOCKET IPV4 DO CLIENTE
    int socketId_Cliente = socket(AF_INET, SOCK_STREAM, NULL);

    if( socketId_Cliente != 0){
        std::cerr << "Falha ao executar o socket do Cliente..." << std::endl;
        exit(EXIT_FAILURE);
    }

    std::cout << "Socket do Cliente criado com sucesso..." << std::endl;

    /// ESTABELECENDO CONEXÃO VIA SOCKETS ENTRE O **CLIENTE** E O SERVIDOR
    if( connect( socketId_Cliente, 
                 (struct sockaddr *) &addrClient, 
                  sizeof(addrClient) 
                ) != 0 ){
        std::cerr << "Falha ao conectar o socket do Cliente e o do Servidor..." << std::endl;
        exit(EXIT_FAILURE);
    }

    std::cout << "Cliente conectado ao Servidor (via sockets)..." << std::endl;

    return 0;

}    