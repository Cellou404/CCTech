import socket 

host = 'localhost'
port = 600

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mySocket.connect((host, port))
except socket.error:
	print("Erreur de connection avec le serveur")
	exit()

print("connection établie avec le serveur !")