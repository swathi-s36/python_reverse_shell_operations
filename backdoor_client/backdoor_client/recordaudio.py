"""
References:
1) Dynamic module installation:
https://stackoverflow.com/questions/12332975/installing-python-module-within-code

2) Recording Audio:
https://www.geeksforgeeks.org/create-a-voice-recorder-using-python/
"""
from installer import install

# import libraries if available, if not install them
try:
	import sounddevice as sd
except:
	install('sounddevice')

try:
	from scipy.io.wavfile import write
except:
	install('scipy')

try:
	import wavio as wv
except:
	install('wavio')

# Sampling frequency
freq = 44100

# Recording duration
duration = 20

# Start recorder with the given values
recording = sd.rec(int(duration * freq),samplerate=freq,channels=2)

# Record the audio for the given duration
sd.wait()

# Converts the NumPy array to audio file
#write("recording0.wav", freq,recording)

# Converts NumPy array to audio file
wv.write("recording.wav",recording,freq,sampwidth=2)
