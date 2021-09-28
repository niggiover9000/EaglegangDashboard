import asyncio
from json import loads
from urllib import request
from random import choice, choices, randint


def update_joke():
    with request.urlopen("https://witzapi.de/api/joke") as url:
        data = loads(url.read().decode())
        file = open("joke.data", "w+")
        file.write(data[0]["text"])
        file.close()
        print("Joke updated:", data[0]["text"])


def update_clickbait():
    headlines = open("clickbait/headlines.data", "r", encoding="utf-8").read().splitlines()
    headline = choice(headlines)
    if "[name2]" in headline:
        names = open("clickbait/names.data", "r", encoding="utf-8").read().splitlines()
        names = choices(names, k=2)
        headline = headline.replace("[name1]", names[0])
        headline = headline.replace("[name2]", names[1])
    elif "[name1]" in headline:
        names = open("clickbait/names.data", "r", encoding="utf-8").read().splitlines()
        name = choice(names)
        headline = headline.replace("[name1]", name)
    if "[object]" in headline:
        objects = open("clickbait/objects.data", "r", encoding="utf-8").read().splitlines()
        _object = choice(objects)
        headline = headline.replace("[object]", _object)
    if "[place]" in headline:
        places = open("clickbait/places.data", "r", encoding="utf-8").read().splitlines()
        place = choice(places)
        headline = headline.replace("[place]", place)
    if "[number]" in headline:
        number = randint(1, 100)
        headline = headline.replace("[number]", str(number))
    file = open("clickbait.data", "w+")
    file.write(headline)
    file.close()
    print("Clickbait updated:", headline)


async def run_tasks():
    while True:
        update_clickbait()
        update_joke()
        await asyncio.sleep(86400)  # One Day


def main():
    print("Started Functions")
    asyncio.run(run_tasks())


if __name__ == '__main__':
    main()
