from flask import Flask, request, render_template
import time
import os

from main import auth

app = Flask(__name__)

os.environ["FLASK_APP"] = __name__
os.environ["FLASK_ENV"] = "development"


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        print(request.json())

    return render_template("test.html")


@app.route("/spotify/login", methods=["GET"])
def spotify_login():
    auth(request.url)
    return request.url


if __name__ == "__main__":
    app.run()
