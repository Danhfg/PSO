## BIBLIOTECAS USADAS
import socket 
import pickle as pickle
import json
import sys
import time
import threading


def capturaConsumoDeMemoria():
    """ Executa o comando de terminal para pegar o consumo de memória

    Returns:
    str:Porcentagem do consumo de memória atual

    """
    comandoConsumoDeMemoria =  "free | grep Mem | awk '{print $3/$2 * 100.0}'"
    return subprocess.check_output(comandoConsumoDeMemoria, stderr=subprocess.STDOUT, shell=True).decode("utf-8")
    

def enviandoConsumoDeMemoria(clientSocket, mensagem):
    """ Enviando continuamente para o servidor o uso atual, em porcentagem, de memória 

    Parameters:
    clientSocket (int): Arquivo descritor do socket do cliente

    Returns:
    str:Porcentagem do consumo de memória atual

    """
    try:
        while True:
            mensagem['memoryUsage'] = capturaConsumoDeMemoria()
            clientSocket.send( pickle.dumps( mensagem ) )
    finally:
        clientSocket.close()
        break


def Main():

    ## 1. VERIFICANDO ARGUMENTOS 
    if len( sys.argv) != 2:
        print("uso: python3 clientSocket.py <nome do cliente>")
        sys.exit()

    informacoesCliente = {"name":sys.argv[1]}  

    host = socket.gethostname()
    portNumber = 14345

    ## 2. CRIANDO SOCKET DO CLIENTE
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    ## 3. CONECTANDO O SOCKET DO CLIENTE AO SOCKET DO SERVIDOR
    clientSocket.connect( (host, portNumber) )

    ## 4. CRIANDO E INICIANDO THREAD QUE SEMPRE ENVIA CONSUMO DE MEMÓRIA PARA O SERVIDOR
    thread_consumoDeMemoria = threading.Thread( target=enviandoConsumoDeMemoria, args=(clientSocket,informacoesCliente,) )
    thread_consumoDeMemoria.start()
 

if __name__ == '__main__': 
    Main() 