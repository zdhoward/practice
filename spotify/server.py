from flask import Flask, request, render_template
import time
import os

app = Flask(__name__)

os.environ["FLASK_APP"] = __name__
os.environ["FLASK_ENV"] = "development"


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        print(request.json())

    return render_template("test.html")


def hello():
    return "Hello, Alishia!"


if __name__ == "__main__":
    app.run()
