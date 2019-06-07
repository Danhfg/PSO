import socket 
import sys
import pickle	# Usada na serializacao da cobra

from Snake import Snake
from Board import Board


HOST = sockets.gethostname()  # (localhost)
PORT_NUMBER = 4324  # Porta usada pelo socket do Servidor
serverSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )      # Criando o socket do servere
    


def main():

	playerName = sys.argv[1]
	playerSnake = Snake( playerSnake )
	playerSnakeBytes = pickle.dumps( playerSnake ) # Serializando cobra do jogador

    serverSocket.connect( (HOST, PORT_NUMBER) )    # Conectando socket do servere ao socket do Servidor
    serverSocket.sendall( playerSnakeBytes )




if __name__ == '__main__':
