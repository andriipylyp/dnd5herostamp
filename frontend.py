from flask import Flask, render_template, request
from datamodel import (
    load_available_races,
    load_available_spells,
    load_available_classes,
    load_available_feats,
    load_names,
    load_available_equipment,
)
from randomize import generate_character, generate_level

AVAILABLE_RACES = load_available_races("races.json")
AVAILABLE_SPELLS = load_available_spells("spells.json")
AVAILABLE_CLASSES = load_available_classes("classes.json")
AVAILABLE_FEATS = load_available_feats("feats.json")
ALAILABLE_FIRST_NAMES = load_names("first-names.json")
AVAILABLE_MIDDLE_NAMES = load_names("middle-names.json")
AVAILABLE_EQUIPMENT = load_available_equipment("equipment.json")

app = Flask(__name__)


class InfoObject:
    def __init__(self):
        self.name = "Example Name"
        self.description = "Example Description"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        level = int(request.form.get("level", 1))
        alignment = int(request.form.get("alignment", 1))
        random = request.form.get("random")
        rating = "UNDEFINED"
        if random == "on":
            rating, level = generate_level()

        generated_sheet = generate_character(
            level,
            rating,
            ALAILABLE_FIRST_NAMES,
            AVAILABLE_MIDDLE_NAMES,
            AVAILABLE_EQUIPMENT,
            AVAILABLE_RACES,
            AVAILABLE_CLASSES,
            AVAILABLE_SPELLS,
            AVAILABLE_FEATS,
            alignment,
        )
        return render_template("index.html", sheet=generated_sheet)
    return render_template("index.html", sheet=None)


if __name__ == "__main__":
    app.run(debug=True)
