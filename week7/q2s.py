import socket
import datetime
import time
def initiateClockServer():
    s=socket.socket()
    port = 8011
    s.bind(("",port))
    s.listen(5)
    while True:
        conn,addr = s.accept()
        print("Server Connected to :",addr)
        conn.send(str(datetime.datetime.now()).encode())
        conn.close()
        
if __name__ == "__main__":
    initiateClockServer()