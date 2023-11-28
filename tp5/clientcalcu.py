import socket
import struct

# Adresse et port du serveur
server_address = ('localhost', 5555)

# Création d'un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    client_socket.connect(server_address)

    # Nombre à envoyer
    number_to_send = 100000

    # Empaquetage de l'entier en format binaire
   bytes_resultat = nombre_entier.to_bytes((nombre_entier.bit_length() + 7) // 8, byteorder='big')

    # Envoi des données empaquetées au serveur
    client_socket.sendall(bytes_resultat)
    print(bytes_resultat)

finally:
    # Fermeture du socket
    client_socket.close()
