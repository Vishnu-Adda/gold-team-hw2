#import socket module
from socket import *
serverPort = 12000
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
#Fill in start
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# print(serverSocket.getsockname())
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode()) 
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()

sys.exit() #Terminate the program after sending the corresponding data 