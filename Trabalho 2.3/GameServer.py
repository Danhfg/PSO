import socket 
import sys
import pickle	# Usada na serializacao da cobra
import random
import time
from _thread import *
import threading 

from Snake import Snake
from Board import Board

delay = 0.1

host = socket.gethostname()  # (localhost)
portNumber = 4324  # Porta usada pelo socket do Servidor
bufferSize = 10000000  # Tamanho do buffer para recebimento de dados na comunicacao via sockets

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

def receivingPlayerName(snakeList, connection ):
    uniquePlayerName = True

    while uniquePlayerName:

        dataBytes = connection.recv( bufferSize )
        newPlayerName = dataBytes.decode('ascii')

        for snake in snakeList:
            if snake.getName() == newPlayerName:
                uniquePlayerName = False
                
        uniquePlayerNameBytes = pickle.dumps(uniquePlayerName)
        connection.sendall( uniquePlayerNameBytes )

    snakeList.append( Snake(newPlayerName) )

    
def sendingSnakeList(snakeList, connection):
    connection.sendall( pickle.dumps(snakeList) )

def sendingApplePosition( applePosition, connection):
    connection.sendall( pickle.dumps(applePosition) )

def receivedSnakeList(connection):
    snakeListBytes = connection.recv( bufferSize )
    snakeList = pickle.loads(snakeListBytes)

    return snakeList

def threaded(connection, snakeList, applePosition): 
    receivingPlayerName(snakeList, connection)

    while True: 
        sendingSnakeList(snakeList , connection)
        sendingApplePosition(applePosition , connection)
        
        snakeList = receivedSnakeList(connection)
   
    c.close() # Fechando a conexao
  

def main():

    newPlayerName = ""

    serverSocket.bind( (host, portNumber) ) 
    serverSocket.listen(5) 
    
    board = Board()
    board.listen()
        
    while True:
        
        c, addr = serverSocket.accept() 

        start_new_thread(threaded, (c, board.getSnakeList(),  board.positionFood()))

        board.update()
        snakeList = board.getSnakeList()
        
        if snakeList != None:
            for snake in snakeList:
                if(snake.getHead().xcor() > 290 or
                    snake.getHead().xcor() < -290 or 
                    snake.getHead().ycor() > 290 or 
                    snake.getHead().ycor() < -290): # Tem que desconectar o usuario

                    #time.sleep(1)
                    x = random.randint(-200, 200)
                    y = random.randint(-200, 200)
                    snake.getHead().goto(x,y)
                    snake.getHead().direction = "stop"

                if snake.getHead().distance(board.getFood()) < 20: # Comer a maça
                    board.changeFood()
                    snake.eats()
                    # adding body of the snake
                    #new_segment = turtle.Turtle()
                    #new_segment.speed(0)
                    #new_segment.shape("square")
                    #new_segment.color("red")
                    #new_segment.penup()
                    #snake.addSegments(new_segment)
                    #segments.append(new_segment) 

                for snk in snakeList: # Matar cobra que encontar no corpo da outra
                    if snk.getName() != snake.getName():
                        for segment in snk.segments:
                            if snake.getHead().distance(segment)< 20:
                                snake.getHead().goto(0,0)
                                snake.getHead().direction = "stop"

                for snk in snakeList: # Matar as cobras que encostarem a cabeça
                    if snk.getName() != snake.getName():
                        #print(snake.getHead().distance(snk.getHead()))
                        if snake.getHead().distance(snk.getHead()) < 20:
                            x = random.randint(-200, 200)
                            y = random.randint(-200, 200)
                            snake.getHead().goto(x,y)
                            snake.getHead().direction = "stop"
                            x = random.randint(-200, 200)
                            y = random.randint(-200, 200)
                            snk.getHead().goto(x,y)
                            snk.getHead().direction = "stop"

                for index in range(len(snake.segments)-1, 0 , -1):
                    x = snake.segments[index-1].xcor()
                    y = snake.segments[index-1].ycor()
                    snake.segments[index].goto(x, y)

                if(len(snake.segments) > 0):
                    x = snake.getHead().xcor()
                    y = snake.getHead().ycor()
                    snake.segments[0].goto(x, y)
                    
                i = random.randint(0,4)
                if i == 0:
                    snake.goUp()
                elif i ==1:
                    snake.goDown()
                elif i ==2:
                    snake.goLeft()
                else:
                    snake.goRight()

                snake.move()

                for segment in snake.segments:
                    if (segment.distance(snake.getHead()) < 20): #matar cobra que comer a sí própria
                        time.sleep(1)
                        snake.goto(0, 0)
                        snake.setDirection("Stop")

                        for segment in snake.segments:
                            segment.goto(1000, 1000)
                        snake.segments.clear()  
            time.sleep(delay)

        # else:
        #     pass

    board.loop()
    serverSocket.close()


if __name__ == '__main__':
    main()