## BIBLIOTECAS USADAS
import sys
import socket 
import pickle
from time import sleep
import threading 
import pandas as pd


def analisandoProcessosDeCliente(conn, listaDeProcessosCliente):
    """ Analisa processos de cliente e envia o comando necessario para excluir os 
    respectivos processo zumbi. 

    Parameters:
    conn (int): Conexao do servidor com o cliente
    listaDeProcessosCliente(str): String contendo a lista de processo com PID e Status

    """

    ## 1. CONVERTENDO PARA TIPO DATAFRAME
    dataFrame_processos = pd.DataFrame([x.split() for x in listaDeProcessosCliente.split('\n')])
    zumbiDataFrame = dataFrame_processos[dataFrame_processos.loc[:,1].str.contains('Z') == True]
    #print(zumbiDataFrame)
    return zumbiDataFrame




def recebendoConsumoDeMemoriaDoCliente(conn, clientes, contadorLogServidor):
    """ Recebe continuamente o consumo de memoria do cliente  

    Parameters:
    conn (int): Conexao do servidor com o cliente
    clientes(dict): Dicionario de informacoes dos clientes conectados

    """
    contadorLog = 1
    #contadorLogMaximo = 15 
    listaDeProcessosCliente = ""

    try:

        while True:
            ## 1. SERVIDOR RECEBE O USO DE MEMÓRIA DO CLIENTE E ATUALIZA COM O QUE TINHA
            #### 1.1 Salva a quantidade de iterações do cliente com os servidor e a quan
            ####      tidade de vezes que o limite de consumo foi ultrapassado. 
            mensagemCliente = pickle.loads( conn.recv(1024) )
            if mensagemCliente['name'] not in clientes.keys():
                clientes[ mensagemCliente['name'] ] = {'memoryUsage':mensagemCliente['memoryUsage'],
                                                       'loops':contadorLog, 'g50':0 , 'zumbis': 0}
            else:
                clientes[ mensagemCliente['name'] ]['memoryUsage'] = mensagemCliente['memoryUsage']
                clientes[ mensagemCliente['name'] ]['loops'] = contadorLog

            
            ## 2. SERVIDOR VERIFICA SE O USO DE MEMÓRIA DO CLIENTE ULTRAPASSOU O PERMITIDO
            if mensagemCliente['memoryUsage'] > 50:
                ## 2.1 Atualiza a qntd de vezes que a mem do cliente ultrapassou o limite
                clientes[ mensagemCliente['name'] ]['g50'] += 1
                ## 3. SERVIDOR PEDE A LISTA DE PROCESSOS E RECEBE DO CLIENTE
                conn.send( pickle.dumps('Quero lista de processos') )
                listaDeProcessosCliente = pickle.loads( conn.recv(10024) )
                ## 4. SERVIDOR ANALISA A LISTA DE PROCESSOS
                zumbiDataFrame = analisandoProcessosDeCliente(conn, listaDeProcessosCliente)
                if zumbiDataFrame.size != 0:
                    clientes[ mensagemCliente['name'] ]['zumbis'] += 1
                    #print(zumbiDataFrame[2].values)
                    for i in zumbiDataFrame[2].values:
                        conn.send( pickle.dumps('kill -HUP ' + str(i)))
                        #conn.send( pickle.dumps('kill -s SIGCHLD ' + str(i)))
                        #ok = pickle.loads( conn.recv(10024) )
                if clientes[ mensagemCliente['name'] ]['loops'] % float(mensagemCliente['max']) == 0:
                    conn.send(pickle.dumps('loops: '+str(clientes[ mensagemCliente['name'] ]['loops'])+"\n"
                                            'g50: '+str(clientes[ mensagemCliente['name'] ]['g50'])+"\n"
                                            'zumbis: '+ str(clientes[ mensagemCliente['name'] ]['zumbis'])))
                    #ok = pickle.loads( conn.recv(10024) )
            
            else:
                conn.send( pickle.dumps('Nao quero lista de processos') )
                    #ok = pickle.loads( conn.recv(10024) )

                
                ## 5. 
              #  if contadorLog == contadorLogMaximo:
            
            ## 4. SERVIDOR ESPERA E ATUALIZA O SEU CONTADOR DE ENVIO DE LOG
            contadorLog += 1

            print(clientes)
            #sleep(3)
    except Exception as e:
        pass


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

