# import socket programming library 
import socket 
#import pickle
import pickle as pickle
import json

# import thread module 
from _thread import *
import threading 

from Snake import Snake
from Board import Board
import turtle
import time
import random

#print_lock = threading.Lock()                                                     ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA
clients = {}
delay = 0.1

# thread fuction 
def threaded(c, addr, b, clients): 
    while True: 
        #b.update()
        #print(len(b.getSnakeList()))

        # data received from client 
        data = c.recv(1024) 
        if not data:
            print( "Client ("  + ") disconnect")
            c.send(pickle.dumps({'disconnect':'True'})) 
            break
        data = pickle.loads(data)
        #print( "Client ("  + ")ask:" + str(data))
        if 'run' in data.keys():
            break
        elif data['name'] not in clients.keys():
            snk = b.getSnake(data['name'])
            fruit = b.getFood()
            segments = []
            if snk != None:
                if snk.getSegments() != []:
                    segments = [(i.xcor(), i.ycor()) for i in snk.getSegments()]
                clients[data['name']] = {'head':(snk.getHead().xcor(), snk.getHead().ycor()),'segments':segments, 'cor':snk.getCor(), 'direction':'stop',
                                      'apple':(fruit.xcor(),fruit.ycor())  }
                data.update( {'head':(snk.getHead().xcor(), snk.getHead().ycor()),'segments':segments, 'cor':snk.getCor(),
                           'apple':(fruit.xcor(),fruit.ycor()) })
        elif 'head' in data.keys():
            clients[data['name']]['direction'] = data['direction']
            #clients[data['name']] = {'head':'','segments':'', 'cor':''}
            #data = {'name':data['name'],'head':'','segments':''}
            # lock released on exit 
 #           print_lock.release()                                            ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA 
            

        # send back reversed string to client 
        c.send(pickle.dumps(clients)) 

    # connection closed 
    c.close() 


def Main(): 
    host = "" 

    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 14345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 

    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
    board = Board()
    board.add_snake(Snake('usuario1'))
    board.add_snake(Snake('usuario2'))
    board.add_snake(Snake('usuario3'))
    board.add_snake(Snake('usuario4'))

    # a forever loop until client wants to exit 
    while True: 
        board.update()

        # establish connection with client 
        c, addr = s.accept() 

        # lock acquired by client 
        #print_lock.acquire()                                                    ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA
        #print('Connected to :', addr[0], ':', addr[1]) 
        print(clients)

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,addr,board ,clients, )) 
        board.update2(clients)
        snakeList = board.getSnakeList()
        
        if snakeList != None:
            for snake in snakeList:
                if snake.getName() in clients.keys():
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
                        
                    i = clients[snake.getName()]['direction']
                    if i == "W":
                        snake.goUp()
                    elif i =="S":
                        snake.goDown()
                    elif i =="A":
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

    s.close() 


if __name__ == '__main__': 
    Main() 