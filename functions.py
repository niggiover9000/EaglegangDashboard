import asyncio
from json import loads
from urllib import request


async def update_joke():
    while True:
        with request.urlopen("https://witzapi.de/api/joke") as url:
            data = loads(url.read().decode())
            file = open("joke.data", "w+")
            file.write(data[0]["text"])
            file.close()
        await asyncio.sleep(86400)  # One Day


def main():
    print("Started Functions")
    asyncio.run(update_joke())


if __name__ == '__main__':
    main()