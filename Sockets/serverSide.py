#!/usr/bin/env python3

import socket  # Biblioteca para sockets

HOST = "127.0.0.1"  # (localhost)
PORT_NUMBER = 4325  # Porta usada pelo socket do Servidor
MESSAGE_SIZE = 40 # Quantidade de caracteres que uma mensagem pode transmitir  


with socket.socket( socket.AF_INET, socket.SOCK_STREAM ) as s:      # Criando o socket do Servidor
    s.bind( ( HOST, PORT_NUMBER ) )     # Ligando o socket do Servidor a porta PORT_NUMBER
    s.listen( )     # Colocando o socket do Servidor para escutar as requisições     
    conn, addr = s.accept()      # Retirando da fila de requisições uma requisição
    with conn:
        print( "Connected by " + addr)
        while True:
            data = conn.recv(MESSAGE_SIZE)  # Recebendo mensagem do socket do Cliente
            print("Cliente disse:" + data)
            if not data or data == "tchau":
                break
            conn.send( input() ) # Enviando mensagem para socket do Cliente