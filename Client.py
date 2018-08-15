from socket import *

HOST = '135.242.165.240' 
PORT = 21567
BUFSIZ = 1024
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    print(data)
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print(data)

tcpCliSock.close()
