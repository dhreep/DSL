import socket

# Define the server's IP and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # Send a request to the server
    s.sendto(b'', (SERVER_HOST, SERVER_PORT))

    # Wait for a response from the server
    data, _ = s.recvfrom(1024)
    print(f"Received time from server: {data.decode()}")
