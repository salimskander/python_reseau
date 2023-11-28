import socket

def encode_message(expression):
    # Encodage de l'expression en UTF-8
    encoded_expression = expression.encode('utf-8')

    # Calcul de la taille du message en octets
    message_size = len(encoded_expression).to_bytes(4, byteorder='big')

    # Assemblage du message
    message = message_size + encoded_expression

    return message

# Configuration du client
server_address = ('127.0.0.1', 9999)

# Création du socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connexion au serveur
    sock.connect(server_address)

    # Saisie de l'expression arithmétique
    expression = input('Entrez une expression arithmétique (ex: 2+x3) : ')

    # Encodage et envoi du message
    encoded_message = encode_message(expression)
    sock.sendall(encoded_message)

    # Réception du résultat
    data = sock.recv(1024)
    result_size = int.from_bytes(data[:4], byteorder='big')
    result = data[4:4 + result_size].decode('utf-8')
    print('Résultat:', result)

finally:
    # Fermeture de la connexion
    sock.close()
