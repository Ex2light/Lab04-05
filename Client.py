import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ("Connecting to {}".format(server_address))
socket.connect(server_address)

try:
    while True:
        data = socket.recv(1024)
        print(data.decode())
        if "END" in data.decode():
            break
        message = input()
        socket.send(str.encode(message))
finally:
    socket.close()