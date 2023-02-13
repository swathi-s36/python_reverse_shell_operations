from termcolor import colored
import socket
import sys,time

def uploadfile(ip,port):

	sock = socket.socket()

	sock.bind(('0.0.0.0',port))
	sock.listen()

#	print ("Listening on port: ",port)

	scon, addr = sock.accept()
#	print (colored(f'Connected with {addr}','green'))

	file = open('client.txt', 'wb')
	line = scon.recv(1024)

	while(line):
	    file.write(line)
	    line = scon.recv(1024)

	print ()
	print (colored('File has been received successfully','green'))
	print ()

	file.close()
	sock.close()
	print ('Connection Closed.')
