import socket

PORT = 8000
SERVER = '192.168.11.5'
ADDR = (SERVER, PORT)
FORMAT = "ascii"

def start():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER, PORT))
        s.listen()

        conn1, addr1 = s.accept()
        print('Connected by pc', addr1 ,',waiting for robot.....')
        conn2, addr2 = s.accept()

        while addr1 == addr2:
            conn2, addr2 = s.accept()
        with conn1:
            print('Connected by robot', addr2 , ',clients connected!')
            while True:
                data = conn1.recv(1024)
                conn2.sendall(data)
                print(data)

start()




# conn1, addr1 = s.accept()
#         print('Connected by pc', addr1, ',waiting for robot.....')
#         conn2, addr2 = s.accept()
#         print('Connected by robot', addr2, ',clients connected!')
#         while True:
#             data = conn1.recv(1024)
#             conn2.sendall(data)
#             print(data)


