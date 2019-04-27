#!/usr/bin/env python3

import socket  # Biblioteca para uso de sockets
import threading # Biblioteca para uso de threads

from subprocess import call # Chamada de sistema por subprocessos

def readADC(number):
	PATH="/sys/bus/iio/devices/iio:device0/in_voltage" +str(number) + "_raw"
	fileADC = open(PATH, "r")
	valueADC = int ( fileADC.readline() )
	fileADC.close()
	return valueADC

############ POTENCIOMETRO ###############

def readPotenciometer():
	return readADC(0)


potenciometer_old = readPotenciometer()

def checkingPotenciometer():    
    global potenciometro_old
    Potenciometro_now = readPotenciometer()
    diference = potenciometer_old - potenciometer_now
	potenciometer_old = potenciometer_now
    if abs(diference) > 5 : 
		print("Houve varicao no Potenciometro", flush=True)
		if diference < 0 : # Movendo-se para à esquerda 
            return "d"
            
        else:  # Movendo-se para a direita
            return "a"
    else:
        return ""

############## LDR ####################

def readLDR():
	return readADC(1)

LDR_old = readLDR()

def checkingLDR():
    global LDR_old
    LDR_now = readLDR()
    diferenca = abs(LDR_old - LDR_now)
    if diferenca > 0.07 :  # Situação em que houve variação no LDR
        print("Houve variacao no LDR", flush=True)
        return "s"
    else:
        return ""

############## BOTAO ####################

def readButton():
	PATH_export = "/sys/class/gpio/export"
	export = open(PATH_export, "a")
	export.write("115")
	PATH = "/sys/class/gpio/gpio115/value"
	fileButton = open(PATH, "r")
	valueButton = int( fileButton.readline() )
	try:
		export.close()
	except:
		pass
	return valueButton

def checkingBotao():
	if readButton() == 1:
		print("Botao foi apertado" , flush=True)
	    return "w"
	else
	    return ""    

############## SOCKET CLIENTE ####################

def runClient():
	HOST = "192.168.7.1"  # (localhost)
    PORT_NUMBER = 4339  # Porta usada pelo socket do Servidor
	MESSAGE_SIZE = 40
	
	with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as s: # Criando socket do Cliente
    s.connect( (HOST, PORT_NUMBER) )    # Conectando socket do Cliente ao socket do Servidor
    print("O socket do Cliente está conectado ao socket do Servidor\n")
	while (True):
		valueLDR=checkingLDR()
		valuePotenciometer=checkingPotenciometer()
		valueButton = checkingButton()		
	
		# Enviando comando capturado do joystick
        if valuePotenciometer != "" :
            s.send( str.encode( valuePotenciometer ) )
        elif valueLDR != "" :
            s.send( str.encode( valueLDR ) ) 
        else:
            if valueBotao != "" :
                s.send( str.encode( valueButton ) )
			else:
				s.send( str.encode("") )
		
		arqTela = open('tela.dat','wb')		
		# Recebendo atualizacao da tela vinda do servidor e imprimindo na tela do cliente
		telaAtualizada = s.recv(MESSAGE_SIZE)
		if not telaAtualizada :
			print( "Houve problema no recebimento da tela atualizada...", flush=True)
			break
		arqTela.write( telaAtualizada )
		arqTela.close()
		call('cat tela.dat', shell=True)
	s.close()

####### THREADS ##########
	
# Criando a threads de checagem
thread_run = threading.Thread(target=runClient)

# Iniciando a threads
thread_run.start()

# Sincronizando a thread
thread_run.join()
