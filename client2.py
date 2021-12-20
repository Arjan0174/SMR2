import socket

FORMAT = 'ascii'

def client_program():

    host = "192.168.11.5"       # Server IP
    port = 8000                 # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input("What would u like to send to the robot? -> ")  # take input

    while message.lower().strip() != 'bye':
        while True:
            client_socket.send(message.encode(FORMAT))  # send message
            # data = client_socket.recv(1024).decode(FORMAT)  # receive response
            # print('Received from server: ' + data)  # show in terminal
            message = input("What would u like to send to the robot? -> ")  # again take input
    client_socket.close()  # close the connection


client_program()