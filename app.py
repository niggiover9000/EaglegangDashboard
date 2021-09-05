from flask import Flask, render_template
from secrets import token_urlsafe

app = Flask(__name__)


@app.route('/')
def eaglegang():  # put application's code here
    return render_template("eaglegang.html")


@app.route('/impressum')
def impressum():  # put application's code here
    return render_template("impressum.html")


def main():
    app.config["SECRET_KEY"] = token_urlsafe(16)
    app.run(debug=True, use_reloader=True, port=80)


if __name__ == '__main__':
    main()
