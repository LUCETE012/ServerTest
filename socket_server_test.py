import socket
from _thread import *

client_sockets=[]


## Sever IP and Port
## HOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'
PORT = 9999

## Processing in thread
## new client, new thread
def threaded(client_socket, addr):
    print('>> Connected by :', addr[0], ':', addr[1])

    ## process until client disconnect
    while True:
        try:
            ## send client if data recieved(echo)
            data = client_socket.recv(1024)
            print('client : ' + repr(data.decode()))

            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break

            print('>> Received from ' + addr[0] + ':', addr[1])

            ## chat to client connecting client
            ## chat to client connecting client except person seding message
            for client in client_sockets:
                if client != client_socket:
                    client.send(data)
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list : ', len(client_sockets))

    client_socket.close()



## Create Socket and Bind
print('>> Server Start with ip : ', HOST)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

def send_threaded(client_socket, addr):
    
    while True:
        try:
            message = input()
            if message == 'quit':
                close_data = message
                break
            client_socket.send(message.encode())
        except ConnectionResetError as e:
            print('>> Error by ' + addr[0], ':', addr[1])
            break

## Client Socket Accept
try:
    while True:
        print('>> Wait')

        client_socket, addr = server_socket.accept()
        client_sockets.append(client_socket)
        start_new_thread(threaded, (client_socket, addr))
        start_new_thread(send_threaded, (client_socket, addr))
        print("# person : ", len(client_sockets))

except Exception as e:
    print('error : ', e)

finally: 
    server_socket.close()