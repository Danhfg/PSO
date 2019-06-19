## BIBLIOTECAS USADAS
import sys
import socket 
import pickle
import json
from time import sleep
import threading 


def recebendoConsumoDeMemoriaDoCliente(conn, clientes, contadorLogServidor):
    """ Recebe continuamente o consumo de memoria do cliente  

    Parameters:
    conn (int): Conexao do servidor com o cliente
    clientes(dict): Dicionario de informacoes dos clientes conectados

    """
    while True:
        mensagemCliente = pickle.loads( conn.recv(1024) )

        ## ATUALIZANDO LISTA DE CLIENTES
        clientes[ mensagemCliente['name'] ] = mensagemCliente['memoryUsage']
        
        if int(mensagemCliente['memoryUsage']) > 50:
            conn.send( pickle.dumps('Quero lista de processos') )

        # else:
        #     sleep(3)

        #     if contadorLogServidor



        print(clientes)


def Main():
    
    if len( sys.argv) >= 2:
        print("uso: python3 serverSocket.py")
        sys.exit() 

    clients = {}
    contadorLogServidor = 15   
    
    host = socket.gethostbyname( socket.gethostname() ) 
    portNumber = 14345

    ## 1. CRIANDO SOCKET DO SERVIDOR E PRENDENDO-SE À PORTA
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    serverSocket.bind( (host, portNumber) ) 
    print("socket binded to post", portNumber) 

    ## 2. SOCKET DO SERVIDOR PASSA ESCUTAR REQUISIÇÕES DE CONEXÃO
    serverSocket.listen(5) 
    print("socket is listening") 

    while True: 

        ## 3. ESTABELECENDO CONEXÃO COM SOCKET DO CLIENTE 
        conn, address = serverSocket.accept()
        thread_consumoDeMemoriaCliente = threading.Thread( target=recebendoConsumoDeMemoriaDoCliente, args=(conn, clients,contadorLogServidor,) )
        thread_consumoDeMemoriaCliente.start() 

    serverSocket.close() 


if __name__ == '__main__': 
    Main() 

