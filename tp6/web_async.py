import aiohttp
import aiofiles
import os
import sys
import asyncio

async def get_content(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error during HTTP request: {e}")
        sys.exit(1)

async def write_content(content, file_path):
    try:
        async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
            await file.write(content)
        print(f"Content written to {file_path}")
    except Exception as e:
        print(f"Error writing content to file: {e}")
        sys.exit(1)

async def main():
    if len(sys.argv) != 2:
        print("Usage: python web_sync.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()

    file_path = './stockurl/web_page_async.html'
    await write_content(content, file_path)

if __name__ == "__main__":
    asyncio.run(main())
