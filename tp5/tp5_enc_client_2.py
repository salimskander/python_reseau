import socket

def send_int(socket, value, num_bytes):
    socket.sendall(value.to_bytes(num_bytes, byteorder='big'))

def send_message(socket, message):
    # Envoie la taille du message
    send_int(socket, len(message), 4)

    # Envoie le message
    send_int(socket, message, len(message).bit_length() // 8 + 1)

    # Envoie la séquence de fin
    send_int(socket, 0, 4)

# Configuration du client
server_address = ('127.0.0.1', 9999)

# Création du socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    sock.connect(server_address)

    # Saisie de l'expression arithmétique
    expression = input('Entrez une expression arithmétique (ex: 2+3) : ')

    # Envoi du message
    send_message(sock, expression)

    # Réception du résultat
    result = int.from_bytes(sock.recv(4), byteorder='big')
    print('Résultat:', result)

finally:
    # Fermeture de la connexion
    sock.close()
