from termcolor import colored
import socket

def downloadfile(ip,port):

	sock = socket.socket()
	sock.connect((ip,port))

	sock.send("secret.txt".encode())

	file = open('server.txt', 'wb')
	line = sock.recv(1024)

	while(line):
	    file.write(line)
	    line = sock.recv(1024)

	print ()
	print (colored('File has been downloaded successfully','green'))
	print ()

	file.close()
	sock.close()
	print ('Connection Closed.')
	print ()
