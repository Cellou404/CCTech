import socket

# On va definir le hot et le port 
# On utilisera le host de la machine

host = 'localhost'
port = 600

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	mySocket.bind((host, port))
	print("Serveur lancé ! \nServeur à l'écoute !")
except socket.error:
	print("ERROR !!! Le serveur n'est pas lancé")
	exit()

mySocket.listen(5)

continuer = True
while continuer:
	connexion, adresse = mySocket.accept()
	print("Nouvelle connection avec IP: {0} PORT: {1} ".format(adresse[0], adresse[1]))
	connexion.close()