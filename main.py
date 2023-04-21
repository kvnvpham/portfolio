from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import date
import json

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    with open("data.json") as file:
        data = json.load(file)

    return render_template("index.html", projects=data)


@app.context_processor
def copyright():
    return {"year": date.today().year}


if __name__ == "__main__":
    app.run(debug=True)