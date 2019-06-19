# Import socket module 
import socket 
import pickle as pickle
import json
import sys
import keyboard
import time

def func(pos, s, d):
    d.update({"direction":pos})
    print(d)
    s.send(pickle.dumps(d))
    #aux = pos
    #print(aux)

def Main(): 
    board = Board()
    data = {"name":sys.argv[1]}
    # local host IP '127.0.0.1' 
    host = socket.gethostname()

    # Define the port on which you want to connect 
    port = 14345

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    # connect to server on local computer 
    s.connect((host,port)) 
    #board.mainWindows.onkeypress(s.send(pickle.dumps(data.update({"direction":"Up"})) ),"Up")
    #board.mainWindows.onkeypress(s.send(pickle.dumps(data.update({"direction":"Down"})) ),"Down")
    #board.mainWindows.onkeypress(s.send(pickle.dumps(data.update({"direction":"Left"})) ),"Left")
    #board.mainWindows.onkeypress(s.send(pickle.dumps(data.update({"direction":"Right"})) ),"Right")

    # message you send to server 
    message = "shaurya says geeksforgeeks"
    connect = False
    while True: 
        #print(board.buttonPressioned())


        # message sent to server 
        #print(data)
        if not connect:
            s.send(pickle.dumps(data) ) 
            connect = True

        # messaga received from server 
        data = s.recv(1024) 
        data = pickle.loads(data)
        if 'apple' in data[sys.argv[1]].keys():
            board.setFood(data[sys.argv[1]]['apple'][0], data[sys.argv[1]]['apple'][1])
            print("AAAAAAAAAAAAAAAAAAAa")

        dataAux = data[sys.argv[1]]
        dataAux.update({'name':sys.argv[1]})
        keyboard.add_hotkey('a', func, args=('A', s, dataAux))
        keyboard.add_hotkey('s', func, args=('S', s, dataAux))
        keyboard.add_hotkey('d', func, args=('D', s, dataAux))
        keyboard.add_hotkey('w', func, args=('W', s, dataAux))

        # print the received message 
        # here it would be a reverse of sent message 
        print('Received from the server :',str(data)) 
        board.update()
        keyboard.wait()
        #time.sleep(0.1)
        #keyboard.remove_all_hotkeys()
        
        #keyboard.wait(tecla)
        # ask the client whether he wants to continue 
        """
        ans = input('\nDo you want to continue(y/n) :') 
        if ans == 'y': 
            continue
        else: 
            break
        """
    # close the connection 
    s.close() 

if __name__ == '__main__': 
    Main() 