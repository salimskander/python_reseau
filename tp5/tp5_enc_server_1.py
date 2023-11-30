import socket

def receive_int(socket, num_bytes):
    data = b''
    while len(data) < num_bytes:
        chunk = socket.recv(num_bytes - len(data))
        if not chunk:
            raise ValueError("Déconnexion inattendue du client.")
        data += chunk
    return int.from_bytes(data, byteorder='big')

# Configuration du serveur
server_address = ('127.0.0.1', 9999)

# Création du socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen()

print('Le serveur écoute sur {}:{}'.format(*server_address))

# Attente de la connexion du client
client_socket, client_address = server_socket.accept()
print('Connexion depuis', client_address)

while True:
    # Réception du header
    header = client_socket.recv(4)
    if not header:
        break

    # Lecture de la taille du message
    msg_len = receive_int(client_socket, 4)

    print(f"Lecture des {msg_len} prochains octets")

    # Une liste qui va contenir les données reçues
    chunks = []

    bytes_received = 0
    while bytes_received < msg_len:
        # Si on reçoit + que la taille annoncée, on lit 1024 par 1024 octets
        chunk = client_socket.recv(min(msg_len - bytes_received, 1024))
        if not chunk:
            raise RuntimeError('Invalid chunk received bro')

        # on ajoute le morceau de 1024 ou moins à notre liste
        chunks.append(chunk)

        # on ajoute la quantité d'octets reçus au compteur
        bytes_received += len(chunk)

    # ptit one-liner pas compliqué à comprendre pour assembler la liste en un seul message
    message_received = b"".join(chunks).decode('utf-8')
    print(f"Received from client: {message_received}")

    # Vérification de la séquence de fin
    fin_sequence = receive_int(client_socket, 4)
    if fin_sequence == 0:
        print("Fin de la séquence détectée")
    else:
        raise RuntimeError("Séquence de fin invalide.")

    # Condition de sortie
    if message_received.lower() == 'exit':
        break

client_socket.close()
server_socket.close()
