import time
import os
import socket
import keyboard

# Here we setup a socket.
defaultPort = 3301
defaultIP = "192.168.0.103"
host = socket.gethostname()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((defaultIP, defaultPort))
s.listen(1)

# Accept incoming connection...
clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")

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
			while keyboard.is_pressed('s'):
				# Send a message to the server when key 's' is pressed.
				msg = 's'
				print(msg)
				clientsocket.send(bytes(msg, 'utf-8'))
			while keyboard.is_pressed('d'):
				# Send a message to the server when key 'd' is pressed.
				msg = 'd'
				print(msg)
				clientsocket.send(bytes(msg, 'utf-8'))
			while keyboard.is_pressed('a'):
				# Send a message to the server when key 'a' is pressed.
				msg = 'a'
				print(msg)
				clientsocket.send(bytes(msg, 'utf-8'))
			# Send a message when no key is being pressed.
			msg = "none"
			print(msg)
			clientsocket.send(bytes(msg, 'utf-8'))
		except Exception as e:
			print(e)
			break

# Start our function.
listenForKeyPress()