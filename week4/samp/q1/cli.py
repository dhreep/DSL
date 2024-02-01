import socket
HOST = '127.0.0.1' # The server's hostname or IP address
PORT = 2053
# The port used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = input("Enter message to server:");
        s.sendall(bytearray(data, 'utf-8'))
        data = s.recv(1024)
        print('Received Connection')
        print('Server:', data.decode())
        if data.decode()=="Stop":
            break;