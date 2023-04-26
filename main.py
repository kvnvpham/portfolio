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


@app.route("/<int:type_id>")
def get_projects(type_id):
    def select_project(category):
        if category["id"] == type_id:
            return True
        return False

    with open("data.json") as file:
        data = json.load(file)

        filtered_data = filter(select_project, data)
        clean_data = list(filtered_data)
    
    return render_template("projects.html", data=clean_data[0])


@app.context_processor
def copyright():
    return {"year": date.today().year}


if __name__ == "__main__":
    app.run(debug=True)