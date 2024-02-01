import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9991
s.connect((host, port))
while True:
    tm = s.recv(1024)
    print(' Current time from Sever :', tm.decode())
    resp = input("Enter the response to the server")
    s.send(resp.encode('ascii'))
    if resp == "stop":
        s.close()
        break
    