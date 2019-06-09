import socket 
import sys
import pickle	# Usada na serializacao da cobra
import random

from Snake import Snake
from Board import Board


#HOST = sockets.gethostname()  # (localhost)
#PORT_NUMBER = 4324  # Porta usada pelo socket do Servidor
#serverSocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )      # Criando o socket do servere
    


def main():

    playerName = sys.argv[1]
    playerSnake = Snake( playerName )
    #playerSnakeBytes = pickle.dumps( playerSnake ) # Serializando cobra do jogador

    #serverSocket.connect( (HOST, PORT_NUMBER) )    # Conectando socket do servere ao socket do Servidor
    #serverSocket.sendall( playerSnakeBytes )
    board = Board()
    board.add_snake(playerSnake)
    while True:
        board.update()
        snakeList = board.getSnakes()
        if snakeList == None:
            for snake in snakeList:
                if(snake.getHead().xcor() > 290 or
                    snake.getHead().xcor() < -290 or 
                    snake.getHead().ycor() > 290 or 
                    snake.getHead().ycor() < -290): # Tem que desconectar o usuario

                    time.sleep(1)
                    #snake.getHead().goto(0,0)
                    #snake.getHead().direction = "stop"

                if snake.getHead().distance(food) < 20: # Comer a maça
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

                for index in range(len(snake.segments)-1, 0 , -1):
                    x = snake.segments[index-1].xcor()
                    y = snake.segments[index-1].ycor()
                    snake.segments[index].goto(x, y)

                if(len(snake.segments) > 0):
                    x = snake.getHead().xcor()
                    y = snake.getHead().ycor()
                    snake.segments[0].goto(x, y)
                    
                move()

                for segment in snake.segments:
                    if (segment.distance(snake.getHead()) < 20):
                        time.sleep(1)
                        snake.goto(0, 0)
                        snake.setDirection("Stop")

                        for segment in snake.segments:
                            segment.goto(1000, 1000)
                        snake.segments.clear()  
            time.sleep(delay)         
        else:
            pass
    board.loop()


if __name__ == '__main__':
    main()