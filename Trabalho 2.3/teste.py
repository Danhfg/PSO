# Import socket module 
import socket 
import pickle as pickle
import json
import sys
import keyboard
import time
from Snake import Snake
from Board import Board

def Main(): 
    board = Board()
    data = {"run":'run'}
    # local host IP '127.0.0.1' 
    host = socket.gethostname()

    # Define the port on which you want to connect 
    port = 14345

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    # connect to server on local computer 
    s.connect((host,port)) 

    # message you send to server 
    connect = False
    #while True: 
        # message sent to server 
    s.send(pickle.dumps(data) ) 

    s.close() 

if __name__ == '__main__': 
    while True:
        Main() 
        time.sleep(0.1)