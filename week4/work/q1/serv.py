import socket
from datetime import datetime

# Define the server's IP and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((SERVER_HOST, SERVER_PORT))
    print(f"UDP server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        # Receive a request
        data, addr = s.recvfrom(1024)
        print(f"Received request from {addr}")

        # Get the current date and time
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Send the current date and time back to the client
        s.sendto(now.encode(), addr)
