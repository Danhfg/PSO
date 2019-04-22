import Adafruit_BBIO.GPIO as GPIO  # Biblioteca para uso de GPIO
import Adafruit_BBIO.ADC as ADC  # Biblioteca para uso de ADC

import socket  # Biblioteca para uso de sockets
import threading # Biblioteca para uso de threads

from time import sleep 

HOST = "127.0.0.1"  # (localhost)
PORT_NUMBER = 4324  # Porta usada pelo socket do Servidor

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) # Criando socket do Cliente

s.connect( (HOST, PORT_NUMBER) )    # Conectando socket do Cliente ao socket do Servidor
print("O socket do Cliente está conectado ao socket do Servidor\n")

# CONFIGURANDO ENTRADAS BEAGLEBONE BLACK
GPIO.setup("P9_27", GPIO.IN) # Configurando entrada GPIO 115 que receberá o sinal do botão
ADC.setup() # Configurando entrada ADC

conteudoLDR_Antigo = ADC.read("AIN0") # Lendo sinal do LDR, inicializando
conteudoPotenciometro_Antigo = ADC.read("AIN1") # Lendo sinal do potenciômetro, inicializando

def checaBotao():
    
    while (True):
        if GPIO.input("P9_27"):
            s.send("w")


def checaLDR():

    global conteudoLDR_Antigo
    
    while( True ):
        conteudoLDR_Atual = ADC.read("AIN0")
        
        diferenca = abs(conteudoLDR_Antigo - conteudoLDR_Atual)

        if( diferenca > 0.02 ):  # Situação em que houve variação no LDR
            s.send("s")
            print("Houve variacao no LDR do Cliente e por isso foi enviado para o Servidor a letra 's'...\n")

        sleep(0.5)


def checaPotenciometro():
    
    global conteudoPotenciometro_Antigo
    
    while( True ):
        conteudoPotenciometro_Atual = ADC.read("AIN1")

        diferenca = conteudoPotenciometro_Antigo - conteudoPotenciometro_Atual

        if( abs(diferenca) > 0.3 )  # Situação em que houve variação no potenciômetro
            print("Houve varicao no Potenciometro de modo que o comando foi ir para a ")
            
            if( diferenca < 0 ) # Movendo-se para à esquerda 
                s.send("a")
                print(" esquerda\n")
            
            else  # Movendo-se para a direita
                s.send("d")
                print(" direita\n")
                
        sleep(0.5)



thread_LDR = threading.Thread(target=checaLDR) # Criando a thread de checagem de LDR
thread_Potenciometro = threading.Thread(target=checaPotenciometro) # Criando a thread de checagem de Potenciometro

# Iniciando as threads
thread_LDR.start()  
thread_Potenciometro.start()

thread_LDR.join()
thread_Potenciometro.join()
