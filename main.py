from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import date

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.context_processor
def copyright():
    return {"year": date.today().year}


if __name__ == "__main__":
    app.run(debug=True)