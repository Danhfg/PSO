#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO  # Biblioteca para uso de GPIO
import Adafruit_BBIO.ADC as ADC  # Biblioteca para uso de ADC

import socket  # Biblioteca para uso de sockets
import threading # Biblioteca para uso de threads

from time import sleep 

def run():
    HOST = "127.0.0.1"  # (localhost)
    PORT_NUMBER = 4324  # Porta usada pelo socket do Servidor
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) # Criando socket do Cliente
    s.connect( (HOST, PORT_NUMBER) )    # Conectando socket do Cliente ao socket do Servidor
    print("O socket do Cliente está conectado ao socket do Servidor\n")

    while (True):
        if( checaPotenciometro() != "" )
            s.send( checaPotenciometro() )
        else if( checaLDR() != "" )
            s.send( checaLDR() ) 
        else
            if( checaBotao() != "" )
                s.send( checaBotao() )       



# CONFIGURANDO ENTRADAS BEAGLEBONE BLACK
GPIO.setup("P9_27", GPIO.IN) # Configurando entrada GPIO 115 que receberá o sinal do botão
ADC.setup() # Configurando entrada ADC

conteudoLDR_Antigo = ADC.read("AIN0") # Lendo sinal do LDR, inicializando
conteudoPotenciometro_Antigo = ADC.read("AIN1") # Lendo sinal do potenciômetro, inicializando

def checaBotao():
    
    while (True):
        if GPIO.input("P9_27"):
            return ("w")
        else
            return ("")    


def checaLDR():

    global conteudoLDR_Antigo
    
    conteudoLDR_Atual = ADC.read("AIN0")
    
    diferenca = abs(conteudoLDR_Antigo - conteudoLDR_Atual)

    if( diferenca > 0.02 ):  # Situação em que houve variação no LDR
        print("Houve variacao no LDR do Cliente e por isso foi enviado para o Servidor a letra 's'...\n")
        return ("s")
        
    else
        return("")


def checaPotenciometro():
    
    global conteudoPotenciometro_Antigo
    
    conteudoPotenciometro_Atual = ADC.read("AIN1")

    diferenca = conteudoPotenciometro_Antigo - conteudoPotenciometro_Atual

    if( abs(diferenca) > 0.3 )  # Situação em que houve variação no potenciômetro
        print("Houve varicao no Potenciometro de modo que o comando foi ir para a ")
        
        if( diferenca < 0 ) # Movendo-se para à esquerda 
            print(" esquerda\n")
            return ("a")
            
        else  # Movendo-se para a direita
            print(" direita\n")
            return("d")
            
    else
        return("")


# Criando a threads de checagem
thread_run = threading.Thread(target=run)

# Iniciando a threads
thread_run.start()

# Sincronizando a thread
thread_run.join()
