import socket 
import sys
import pickle	# Usada na serializacao da cobra

from Snake import Snake
from Board import Board


HOST = sockets.gethostname()  # (localhost)
PORT_NUMBER = 4324  # Porta usada pelo socket do Servidor
clientSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )      # Criando o socket do Cliente
    


def main():

	playerName = sys.argv[1]
	playerSnake = Snake( playerSnake )
	playerSnakeBytes = pickle.dumps( playerSnake ) # Serializando cobra do jogador

    clientSocket.connect( (HOST, PORT_NUMBER) )    # Conectando socket do Cliente ao socket do Servidor
    clientSocket.sendall( playerSnakeBytes )




if __name__ == '__main__':
