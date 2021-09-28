from flask import Flask, render_template
from secrets import token_urlsafe
from os import listdir


app = Flask(__name__)


@app.route('/')
def eaglegang():
    joke = _joke_reader()
    clickbait = _clickbait_reader()
    emotes = listdir("static/img/moneyboy_emotes")
    return render_template("eaglegang.html", joke=joke, clickbait=clickbait, emotes=emotes)


def _joke_reader():
    file = open("joke.data", "r")
    joke = file.read()
    file.close()
    return joke


def _clickbait_reader():
    file = open("clickbait.data", "r")
    clickbait = file.read()
    file.close()
    return clickbait


@app.route('/impressum')
def impressum():  # put application's code here
    return render_template("impressum.html")


def main(port=5000):
    print("Started App")
    app.config["SECRET_KEY"] = token_urlsafe(16)
    app.run(debug=False, use_reloader=False, port=port, host="0.0.0.0")


if __name__ == '__main__':
    main()
