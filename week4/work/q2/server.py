import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 10000)
    server_socket.bind(server_address)
    while True:
        data, address = server_socket.recvfrom(4096)
        print(f"Received {data} from {address}")
        data = input("Enter a message: ").encode()
        if data:
            sent = server_socket.sendto(data, address)
            print(f"Sent {sent} bytes back to {address}")

if __name__ == "__main__":
    server()
