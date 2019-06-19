# import socket programming library 
import socket 
#import pickle
import pickle as pickle
import json

# import thread module 
from _thread import *
import threading 


#print_lock = threading.Lock()                                                     ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA
clients = {}
delay = 0.1

# thread fuction 
def threaded(c, addr, b, clients): 
    while True: 

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

    # a forever loop until client wants to exit 
    while True: 

        # establish connection with client 
        c, addr = s.accept() 

    s.close() 


if __name__ == '__main__': 
    Main() 