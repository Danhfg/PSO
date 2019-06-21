## BIBLIOTECAS USADAS
import socket 
import pickle as pickle
import json
import sys
from time import sleep
import threading
import subprocess


def listaDeProcessos():
    """ Executa o comando de terminal para pegar a lista de processos

    Returns:
    str:Lista de processos

    """
    comandoListaDeProcesso = "ps -eo user,pid,stat"
    return subprocess.check_output(comandoListaDeProcesso, stderr=subprocess.STDOUT, shell=True).decode("utf-8")
  

def capturaConsumoDeMemoria():
    """ Executa o comando de terminal para pegar o consumo de memória

    Returns:
    str:Porcentagem do consumo de memória atual

    """
    comandoConsumoDeMemoria =  "free | grep Mem | awk '{print $3/$2 * 100.0}'"
    return float(subprocess.check_output(comandoConsumoDeMemoria, stderr=subprocess.STDOUT, shell=True).decode("utf-8"))
    

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

    try:
        while True:
            ## 4. ENVIA CONSUMO DE MEMÓRIA PARA O SERVIDOR
            informacoesCliente['memoryUsage'] = capturaConsumoDeMemoria()
            clientSocket.send( pickle.dumps( informacoesCliente ) )

            respostaServidor = pickle.loads(clientSocket.recv(1024))

            print( respostaServidor )

            if respostaServidor == 'Quero lista de processos':
                clientSocket.send( pickle.dumps( listaDeProcessos() ) )
                
            sleep(3)
    finally:
        clientSocket.close()


if __name__ == '__main__': 
    Main() 