import time
import os
import socket
#import RPi.GPIO as GPIO

# Set up GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(18, GPIO.OUT)

#Set up the socket:
defaultPort = 3301
defaultIP = "192.168.0.103"
host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Here we conect to the server. AKA Raspberry Pi.
s.connect((defaultIP, defaultPort))

# Define a function to listen for messages:
def listenForMsg():
	# While code is running:
	while True:
		try:
			# Recive messages.
			msg = s.recv(1024)
			# Decode message.
			msg = msg.decode('utf-8')
			# If message = 'w' turn led on.
			if msg == "w":
				#GPIO.output(18, GPIO.HIGH)
				print(msg)
			# If message != 'w' turn led off.
			else:
				print(msg)
				#GPIO.output(18, GPIO.LOW)
		except Exception as e:
			print(e)
			pass

listenForMsg()