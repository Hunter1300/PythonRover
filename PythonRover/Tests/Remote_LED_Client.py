import time
import os
import socket
import keyboard

# Here we setup a socket.
defaultPort = 3301
defaultIP = 192.168.0.108
host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Here we conect to the server. AKA Raspberry Pi.
connect(defaultIP, defaultPort)

# Define a function.
def listenForKeyPress():
	# While the program is running:
	while True:
		try:
			while keyboard.is_pressed('w'):
				# Send a message to the server when key 'w' is pressed.
				msg = "w"
				print(msg)
				clientsocket.send(bytes(msg, 'utf-8'))
			# Send a message when 'w' is not being pressed.
			msg = "none"
			print(msg)
			clientsocket.send(bytes(msg, 'utf-8'))
		except:
			pass

# Start our function.
listenForKeyPress()