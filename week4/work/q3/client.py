import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('172.16.59.92', 10200))
    while True:
        
        data = input("Enter a message: ")
        client.send(data.encode('utf-8'))
        print('Recieved from server: ',client.recv(1024).decode('utf-8'))
        if data == 'stop':
            client.close()
            break

if __name__ == "__main__":
    start_client()
