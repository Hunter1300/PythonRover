import time
import os
import socket
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

#Set up the socket:
defaultPort = 3301
defaultIP = "192.168.0.108"
host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(defaultIP, defaultPort)
s.listen(5)

# Accept incoming connection...
clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")

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
				GPIO.output(18, GPIO.HIGH)
			# If message != 'w' turn led off.
			else:
				GPIO.output(18, GPIO.LOW)
		except Exception as e:
			print(e)
			pass