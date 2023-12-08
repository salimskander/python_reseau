import asyncio

async def handle_client(reader, writer):
    # Récupérer les informations sur le client
    client_address = writer.get_extra_info('peername')
    print(f"Client connecté depuis {client_address}")

    # Lire les données du client
    data = await reader.read(100)
    message = data.decode()
    print(f"Message du client : {message}")

    # Envoyer un message de salutation au client
    response = f"Hello {client_address[0]}:{client_address[1]}"
    writer.write(response.encode())

    # Fermer la connexion
    print("Fermeture de la connexion avec le client")
    writer.close()

async def main():
    # Créer un serveur
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    # Obtenir l'adresse du serveur
    addr = server.sockets[0].getsockname()
    print(f'Serveur en attente de connexion sur {addr}')

    

    # Attendre que le serveur soit fermé
    async with server:
        await server.serve_forever()

# Lancer le serveur
asyncio.run(main())
