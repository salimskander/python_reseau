import asyncio
import aioconsole

async def async_input(writer):
    while True:
        input = await aioconsole.ainput("vous : ")
        writer.write(input.encode())
        await writer.drain()

async def async_receive(reader):
    while True:
        data = await reader.read(1024)
        if data:
            print(data.decode())
            else:
                break
async def main():
    server_address = ('127.0.0.1', 8888)
    reader, writer = await asyncio.open_connection(server_address)
    tasks = [ async_input, async_receive() ]
    await asyncio.gather(*tasks)
    


    finally:
        # Fermer la connexion
        print("Fermeture de la connexion avec le serveur")
        writer.close()
        await writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())