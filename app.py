from flask import Flask, render_template
from secrets import token_urlsafe


app = Flask(__name__)


@app.route('/')
def eaglegang():
    joke = _joke_reader()
    return render_template("eaglegang.html", joke=joke)


def _joke_reader():
    file = open("joke.data", "r")
    joke = file.read()
    file.close()
    return joke


@app.route('/impressum')
def impressum():  # put application's code here
    return render_template("impressum.html")


def main():
    print("Started App")
    app.config["SECRET_KEY"] = token_urlsafe(16)
    app.run(debug=False, use_reloader=False, port=5000, host="0.0.0.0")


if __name__ == '__main__':
    main()
