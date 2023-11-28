import socket

def decode_message(data):
    # Décode la taille du message
    message_size = int.from_bytes(data[:4], byteorder='big')

    # Décode le message
    message = data[4:4 + message_size].decode('utf-8')

    # Retourne le message et le reste des données
    return message, data[4 + message_size:]

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
    # Réception des données
    data = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        data += chunk

    # Décodage du message
    message, _ = decode_message(data)
    print('Message reçu:', message)

    # Évaluation de l'expression
    try:
        result = str(eval(message))
    except Exception as e:
        result = 'Erreur: {}'.format(str(e))

    # Envoi du résultat au client
    result_message = result.encode('utf-8')
    result_size = len(result_message).to_bytes(4, byteorder='big')
    client_socket.sendall(result_size + result_message)

finally:
    # Fermeture des connexions
    client_socket.close()
    server_socket.close()
