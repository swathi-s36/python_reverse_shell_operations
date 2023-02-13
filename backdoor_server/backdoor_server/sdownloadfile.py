from termcolor import colored
import socket

def downloadfile(ip,port):

	sock = socket.socket()
	sock.bind(('0.0.0.0', port))

	sock.listen()
	scon, addr = sock.accept()

	filepath = scon.recv(1024).decode()

	file = open(filepath, 'rb')
	line = file.read(1024)

	while(line):
		scon.send(line)
		line = file.read(1024)

	file.close()

	print ()
	print (colored('File has been transferred successfully','green'))
	print ()

	sock.close()

	print ("Socket closed")
	print ()
