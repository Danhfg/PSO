import socket 
import sys
import pickle	# Usada na serializacao da cobra

from Snake import Snake
from Board import Board

host = socket.gethostname()  # (localhost)
portNumber = 4324  # Porta usada pelo socket do Servidor
bufferSize = 10000000  # Tamanho do buffer para recebimento de dados na comunicacao via sockets

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
		
def receivingSnakeList():
	snakeListBytes = clientSocket.recv( bufferSize )
	snakeList = pickle.loads(snakeList)
 	
	return snakeList

def sendingSnakeComand(board, snakeList, playerName):

	for snake in snakeList:
		if snake.getName() == playerName:
			board.listenEspecificSnake(snake)
	
	snakeListBytes = pickle.dumps(snakeList)
	clientSocket.sendall( snakeListBytes )
  		

def main():

	board = Board()

	playerName = sendingPlayerName()

	while True :
		
		applePosition = receivingApplePosition()
		board.setFoodPosition( applePosition.getPosition() )

		snakeList = receivingSnakeList()
		board.setSnakeList(snakeList)

		board.loop()

		sendingSnakeComand(board, snakeList, playerName)

if __name__ == '__main__':
    main()