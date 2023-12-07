import asyncio


async def sleep_and_print():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.5)

# sleep_and_print()
# sleep_and_print()
loop = asyncio.get_event_loop()

task = [
    loop.create_task(sleep_and_print()),
    loop.create_task(sleep_and_print())
]

loop.run_until_complete(asyncio.wait(task))
loop.close()

