import socket 

from _thread import *
import threading 

from Board import Board

#print_lock = threading.Lock()                                                     ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA

def threaded(c, addr): 
    while True: 

        playerName = c.recv(1024) 
        print( "Client (" + str(addr) + ")ask:" + data.decode() )

        if not data: 
            print( "Client (" + str(addr) + ") disconnect")
            break

        c.send(data) 

    c.close() 


def Main(): 
    host = "" 

    port = 14343
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 

    s.listen(5) 
    print("socket is listening") 

    board = Board()

    while True: 

        c, addr = s.accept() 

        #print_lock.acquire()                                                    ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA
        print('Connected to :', addr[0], ':', addr[1]) 

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,addr ,)) 
    s.close() 


if __name__ == '__main__': 
    Main() 