import socket
from threading import Thread

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        print(f"Received: {request.decode('utf-8')}")
        data = input("Enter a message: ")
        client_socket.send(data.encode('utf-8'))
        if data == 'stop':
            client_socket.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('172.16.59.92', 10200))
    server.listen()
    print("Server started...")

    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")
        Thread(target=handle_client, args=(client, )).start()

if __name__ == "__main__":
    start_server()
