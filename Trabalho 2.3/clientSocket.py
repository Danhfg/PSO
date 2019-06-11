# Import socket module 
import socket 
import pickle as pickle
import json
import sys

from Board import Board

def Main(): 
    data = {"name":sys.argv[1]}
    
    # local host IP '127.0.0.1' 
    host = socket.gethostname()

    # Define the port on which you want to connect 
    port = 14342

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    # connect to server on local computer 
    s.connect((host,port)) 

    board = Board()

    while True: 

        # message sent to server 
        print(data)
        s.send(pickle.dumps(data) ) 

        # # messaga received from server 
        # data = s.recv(1024) 
        # data = pickle.loads(data)

        # # print the received message 
        # # here it would be a reverse of sent message 
        # print('Received from the server :',str(data)) 
        
        board.update()    
        # send button pressioned
        data['comando'] = board.buttonPressioned()
        # s.send( pickle.dumps(data) ) 
        print( data )

        # ask the client whether he wants to continue 
        # ans = input('\nDo you want to continue(y/n) :') 
        # if ans == 'y': 
            # continue
        # else: 
            # break
    # close the connection 
    s.close() 

if __name__ == '__main__': 
    Main() 