import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    while True:
        message = input("Enter a message: ")
        client_socket.sendto(message.encode(), server_address)
        data, server = client_socket.recvfrom(4096)
        print(f"Received {data.decode()} from {server}")

if __name__ == "__main__":
    client()
