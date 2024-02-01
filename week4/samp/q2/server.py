import time
import socket
servsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9991
servsock.bind((host,port))
servsock.listen(5)
while True:
    clisock,addr = servsock.accept()
    print('Connected from ',str(addr))
    currtime = time.ctime(time.time())+'\r\n'
    clisock.send(currtime.encode('ascii'))
    repl = clisock.recv(1024)
    print(repl.decode())
    if repl.decode() == "stop":
        clisock.close()
        break
