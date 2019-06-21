## BIBLIOTECAS USADAS
import sys
import socket 
import pickle
from time import sleep
import threading 


def analisandoProcessosDeCliente(conn, listaDeProcessosCliente):
    """ Analisa processos de cliente e envia o comando necessario para excluir os 
    respectivos processo zumbi. 

    Parameters:
    conn (int): Conexao do servidor com o cliente
    listaDeProcessosCliente(str): String contendo a lista de processo com PID e Status

    """

    ## 1. CONVERTENDO PARA TIPO DATAFRAME
    dataFrame_processos = pd.DataFrame([x.split() for x in lProcessos.split('\n')])




def recebendoConsumoDeMemoriaDoCliente(conn, clientes, contadorLogServidor):
    """ Recebe continuamente o consumo de memoria do cliente  

    Parameters:
    conn (int): Conexao do servidor com o cliente
    clientes(dict): Dicionario de informacoes dos clientes conectados

    """
    contadorLog = 0
    contadorLogMaximo = 15 
    listaDeProcessosCliente = ""

    try:

        while True:
            ## 1. SERVIDOR RECEBE O USO DE MEMÓRIA DO CLIENTE E ATUALIZA COM O QUE TINHA
            mensagemCliente = pickle.loads( conn.recv(1024) )
            clientes[ mensagemCliente['name'] ] = mensagemCliente['memoryUsage']
            
            ## 2. SERVIDOR VERIFICA SE O USO DE MEMÓRIA DO CLIENTE ULTRAPASSOU O PERMITIDO
            if mensagemCliente['memoryUsage'] > 50:
                ## 3. SERVIDOR PEDE A LISTA DE PROCESSOS E RECEBE DO CLIENTE
                conn.send( pickle.dumps('Quero lista de processos') )
                listaDeProcessosCliente = pickle.loads( conn.recv(10024) )
                ## 4. SERVIDOR ANALISA A LISTA DE PROCESSOS
                analisandoProcessosDeCliente(conn, listaDeProcessosCliente)
            
            else:
                conn.send( pickle.dumps('Nao quero lista de processos') )
                
                ## 5. 
              #  if contadorLog == contadorLogMaximo:
            
            ## 4. SERVIDOR ESPERA E ATUALIZA O SEU CONTADOR DE ENVIO DE LOG
            ++ contadorLog
            sleep(3)

            print(clientes)
    finally:
        print('Erro!')


def Main():
    
    ## VERIFICANDO ARGUMENTOS PASSADOS EM LINHA DE COMANDO
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

