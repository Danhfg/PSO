## BIBLIOTECAS USADAS
import sys
import socket 
import pickle
import json
import threading 


#print_lock = threading.Lock()                                                     ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA

# # thread fuction 
# def threaded(c, addr, b, clients): 
#     while True: 

#         # data received from client 
#         data = c.recv(1024) 
#         if not data:
#             print( "Client ("  + ") disconnect")
#             c.send(pickle.dumps({'disconnect':'True'})) 
#             break
#         data = pickle.loads(data)
#         #print( "Client ("  + ")ask:" + str(data))
#         if 'run' in data.keys():
#             break

#         elif data['name'] not in clients.keys():
#             snk = b.getSnake(data['name'])
#             fruit = b.getFood()
#             segments = []
#             if snk != None:
#                 if snk.getSegments() != []:
#                     segments = [(i.xcor(), i.ycor()) for i in snk.getSegments()]
#                 clients[data['name']] = {'head':(snk.getHead().xcor(), snk.getHead().ycor()),'segments':segments, 'cor':snk.getCor(), 'direction':'stop',
#                                       'apple':(fruit.xcor(),fruit.ycor())  }
#                 data.update( {'head':(snk.getHead().xcor(), snk.getHead().ycor()),'segments':segments, 'cor':snk.getCor(),
#                            'apple':(fruit.xcor(),fruit.ycor()) })
#         elif 'head' in data.keys():
#             clients[data['name']]['direction'] = data['direction']
#             #clients[data['name']] = {'head':'','segments':'', 'cor':''}
#             #data = {'name':data['name'],'head':'','segments':''}
#             # lock released on exit 
#  #           print_lock.release()                                            ## CASO DESEJE MULTIPLOS CLIENTE, COMENTE ESTA LINHA 
            

#         # send back reversed string to client 
#         c.send(pickle.dumps(clients)) 

#     # connection closed 
#     c.close() 

def recebendoConsumoDeMemoriaDoCliente(conn, clientes):
    mensagemCliente = pickle.loads( conn.recv(1024) )
    print( mensagemCliente['name'] + mensagemCliente['memoryUsage'] )




def Main():
    
    if len( sys.argv) >= 2:
        print("uso: python3 serverSocket.py")
        sys.exit() 

    clients = {}
    
    host = socket.gethostbyname( socket.gethostname() ) 
    portNumber = 14345

    ## 1. CRIANDO SOCKET DO SERVIDOR E PRENDENDO-SE À PORTA
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    serverSocket.bind( (host, portNumber) ) 
    print("socket binded to post", portNumber) 

    ## 2. SOCKET DO SERVIDOR PASSA ESCUTAR REQUISIÇÕES DE CONEXÃO
    serverSocket.listen(5) 
    print("socket is listening") 

    while True: 

        ## 3. ESTABELECENDO CONEXÃO COM SOCKET DO CLIENTE 
        conn, address = serverSocket.accept()
        thread_consumoDeMemoriaCliente = threading.Thread( target=recebendoConsumoDeMemoriaDoCliente, args=(conn, clients,) )
        thread_consumoDeMemoriaCliente.start() 

    serverSocket.close() 


if __name__ == '__main__': 
    Main() 