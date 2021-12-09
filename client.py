import socket

FORMAT = 'ascii'                                                                # Format
host = "192.168.11.5"                                                           # Server IP
port = 8000                                                                     # socket server port number

def client_program():

    client_socket = socket.socket()                                             # instantiate
    client_socket.connect((host, port))                                         # connect to the server
    message = input("What would u like to send to the robot? -> ")              # take input

    while message.lower().strip() != 'bye':
        while True:
            client_socket.send(message.encode(FORMAT))                          # send message
            message = input("What would u like to send to the robot? -> ")      # again take input
    client_socket.close()                                                       # close the connection


client_program()