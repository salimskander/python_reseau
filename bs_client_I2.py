import socket
import sys

# On définit la destination de la connexion
host = '10.0.2.15'  # IP du serveur
port = 13337              # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect((host, port))
print(f'Connecté avec succès au serveur {host} sur le port {port}')

msg_input = input('envoie un msg au serveur')
# note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

# Envoi de data bidon
s.sendall(msg_input.encode())

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024)

# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(f"Le serveur a répondu {repr(data)}")

sys.exit(0)

