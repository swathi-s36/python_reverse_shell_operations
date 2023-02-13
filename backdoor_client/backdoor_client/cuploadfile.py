from termcolor import colored
import socket
import sys

def uploadfile(ip,port):

#	print (f'IP: {ip}, Port: {port}')

	sock = socket.socket()
	sock.connect((ip,port))
#	sock.bind((ip, port))

	filepath = input("Enter full filepath of file to upload: ")

	file = open(filepath, 'rb')
	line = file.read(1024)

	while(line):
		sock.send(line)
		line = file.read(1024)

	file.close()

	print ()
	print (colored('File has been transferred successfully','green'))
	print ()

	sock.close()
	print ("Socket closed")
