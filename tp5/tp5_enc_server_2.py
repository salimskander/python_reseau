import socket

def receive_int(socket, num_bytes):
    data = b''
    while len(data) < num_bytes:
        chunk = socket.recv(num_bytes - len(data))
        if not chunk:
            raise ValueError("Déconnexion inattendue du client.")
        data += chunk
    return int.from_bytes(data, byteorder='big')

def receive_message(socket):
    # Lit la taille du message
    message_size = receive_int(socket, 4)

    # Lit le message
    message = receive_int(socket, message_size)

    # Vérifie la séquence de fin
    fin_sequence = receive_int(socket, 4)
    if fin_sequence != 0:
        raise ValueError("Séquence de fin invalide.")

    return message

# Configuration du serveur
server_address = ('127.0.0.1', 9999)

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print('Le serveur écoute sur {}:{}'.format(*server_address))

# Attente de la connexion du client
client_socket, client_address = server_socket.accept()
print('Connexion depuis', client_address)

try:
    # Réception du message
    message = receive_message(client_socket)
    print('Message reçu:', message)

    # Évaluation de l'expression
    try:
        result = eval(message)
    except Exception as e:
        result = 'Erreur: {}'.format(str(e))

    # Envoi du résultat au client
    client_socket.sendall(result.to_bytes(4, byteorder='big'))

finally:
    # Fermeture des connexions
    client_socket.close()
    server_socket.close()
