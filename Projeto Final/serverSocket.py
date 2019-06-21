## BIBLIOTECAS USADAS
import sys
import socket 
import pickle
from time import sleep
import threading 

def recebendoConsumoDeMemoriaDoCliente(conn, clientes, contadorLogServidor):
    """ Recebe continuamente o consumo de memoria do cliente  

    Parameters:
    conn (int): Conexao do servidor com o cliente
    clientes(dict): Dicionario de informacoes dos clientes conectados

    """
    contadorLog = 0
    contadorLogMaximo = 15 

    while True:
        ## 1. SERVIDOR RECEBE O USO DE MEMÓRIA DO CLIENTE E ATUALIZA COM O QUE TINHA
        mensagemCliente = pickle.loads( conn.recv(1024) )
        clientes[ mensagemCliente['name'] ] = mensagemCliente['memoryUsage']
        
        ## 2. SERVIDOR VERIFICA SE O USO DE MEMÓRIA DO CLIENTE ULTRAPASSOU O PERMITIDO
        if int(mensagemCliente['memoryUsage']) > 50:
            ## 3. SERVIDOR PEDE A LISTA DE PROCESSOS E RECEBE DO CLIENTE
            conn.send( pickle.dumps('Quero lista de processos') )
            listaDeProcessosCliente = pickle.loads( conn.recv(1024) )
            print( listaDeProcessosCliente )
            sleep(3)
        
        else:
            conn.send( pickle.dumps('Nao quero lista de processos') )
            sleep(3)

            ## 4. SERVIDOR ESPERA E ATUALIZA O SEU CONTADOR DE ENVIO DE LOG
         #   ++contadorLog
            
            ## 5. 
          #  if contadorLog == contadorLogMaximo:
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

