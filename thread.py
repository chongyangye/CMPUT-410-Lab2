#CMPUT 410 Lab2 Chongyang Ye
import socket
import sys
try:
    import thread
except ImportError:
    import _thread as thread
    

def clientthread(conn):
    while 1:
        data =conn.recv(1024)

        reply ='Hello '+ str(data)
        conn.sendall(reply.encode("UTF-8"))    
   

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    sys.exit()
HOST = '' 
PORT = 8888 # Arbitrary non-privileged port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    sys.exit()
     
 
s.listen(10)

while 1:
 
#wait to accept a connection - blocking call
    conn, addr = s.accept()
    thread.start_new_thread(clientthread,(conn,))

conn.close()
s.close()    
