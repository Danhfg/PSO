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

# thread fuction 
def threaded(c, addr): 
    while True: 

        # data received from client 
        data = c.recv(1024) 
        data = pickle.loads(data)
        print( "Client ("  + ")ask:" + str(data))
#         if data['name'] not in clients.keys():
#             clients[data['name']] = {'head':'','segments':''}
#             data =  {'name':data['name'],'head':'','segments':''}
#         else:
#             break

#         if not data: 
#             print( "Client ("  + ") disconnect")
#             break
#             # lock released on exit 
#  #           print_lock.release()                                            ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA 
            

#         # send back reversed string to client 
#         c.send(pickle.dumps(data)) 

#         # data comand pressioned received from client 
#         data = c.recv(1024) 
#         data = pickle.loads(data)

#         print( "Client ("  + ") ask:" + str(data))
        

    # connection closed 
    c.close() 


def Main(): 
    host = "" 

    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 14342
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

        # lock acquired by client 
        #print_lock.acquire()                                                    ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA
        #print('Connected to :', addr[0], ':', addr[1]) 
        print(clients)

        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,addr ,)) 
    s.close() 


if __name__ == '__main__': 
    Main() 