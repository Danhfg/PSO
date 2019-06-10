import socket
import sys
import pickle	

from Board import Board

host = socket.gethostname()
port = 14343

clientSocket = socket.socket( socket.AF_INET,socket.SOCK_STREAM )  

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


def main():

    board = Board()

	playerName = sendingPlayerName()

    while True:

        board.update()
        print( board.buttonPressioned() )
		clientSocket.send


if __name__ == "__main__":
    main()