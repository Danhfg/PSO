## BIBLIOTECAS USADAS
import socket 
import pickle as pickle
import json
import sys
import os
from time import sleep
import threading
import subprocess


def listaDeProcessos():
    """ Executa o comando de terminal para pegar a lista de processos

    Returns:
    str:Lista de processos

    """
    comandoListaDeProcesso = "ps -eo pid,stat,ppid"
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
    if len( sys.argv) != 4:
        print("uso: python3 clientSocket.py <nome do cliente> <IP Servidor> <tempo máximo>")
        sys.exit()

    informacoesCliente = {"name":sys.argv[1], "max":sys.argv[3]}  

    host = sys.argv[2]
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

            #print( respostaServidor )
            if "kill" in respostaServidor:
                os.system(respostaServidor)
                clientSocket.send( pickle.dumps( listaDeProcessos() ) )
            elif "loops" in respostaServidor:
                #os.system(respostaServidor)
                os.system("echo \""+respostaServidor + "\" > zumbi.log")
                clientSocket.send( pickle.dumps( listaDeProcessos() ) )
            elif respostaServidor == 'Quero lista de processos':
                clientSocket.send( pickle.dumps( listaDeProcessos() ) )
            elif respostaServidor == 'Nao quero lista de processos':
                pass

            sleep(1)
    finally:
        clientSocket.close()


if __name__ == '__main__': 
    Main() 