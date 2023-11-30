import socket
import re

def is_valid_expression(expression):
    # Vérifie que l'expression est une opération arithmétique simple
    pattern = re.compile(r'^\d+\s*[+*/-]\s*\d+$')
    return bool(pattern.match(expression))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))

while True:
    # Saisie de l'expression arithmétique
    expression = input('Enter a simple arithmetic expression: ')

    # Vérification de l'expression
    if not is_valid_expression(expression):
        print("Invalid expression. Please enter a valid expression.")
        continue

    # Encodage du message
    encoded_msg = expression.encode('utf-8')

    # Calcul de la taille du message
    msg_len = len(encoded_msg)

    # Création du header
    header = msg_len.to_bytes(4, byteorder='big')

    # Concaténation du header avec le message
    payload = header + encoded_msg

    # Envoi sur le réseau
    sock.send(payload)

    # Condition de sortie
    if expression.lower() == 'exit':
        break

sock.close()
