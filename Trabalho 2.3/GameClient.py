import socket 
import sys
import pickle	# Usada na serializacao da cobra

from Snake import Snake
from Board import Board

host = socket.gethostname()  # (localhost)
portNumber = 4324  # Porta usada pelo socket do Servidor
bufferSize = 8192  # Tamanho do buffer para recebimento de dados na comunicacao via sockets

clientSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) # Criando o socket do Cliente

def sendingPlayerName():
	playerName = sys.argv[1]

	clientSocket.connect( (host, portNumber) )

	while True:
		clientSocket.send( playerName.encode('ascii') )
		dataBytes = clientSocket.recv( bufferSize )
		uniqueName = pickle.loads(dataBytes)

		if uniqueName:
			break

		return playerName
		
def receivingScreen(board):
	dataBytes = clientSocket.recv( bufferSize )
	board = pickle.loads(dataBytes)
 
def findingMySnake(board, playerName):
	snakeList = board.getSnakes()

	for snake in snakeList:
		if snake.getName() == playerName:
			return snake

def sendingSnakeComand(board, snake):
	board.listenEspecificSnake(snake)
	boardBytes = pickle.dumps(board)
	clientSocket.sendall( boardBytes )
  		

def main():

	sendingPlayerName()

	while True :
		receivingScreen(board)
		
		board.loop()

		mySnake = findingMySnake(board)	
		sendingSnakeComand(board, mySnake)

if __name__ == '__main__':
    main()