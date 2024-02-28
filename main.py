from datamodel import (
    load_available_races,
    load_available_spells,
    load_available_classes,
    load_available_feats,
    load_names,
    load_available_equipment,
)

from randomize import generate_character_name, generate_character

available_races = load_available_races("races.json")
available_spells = load_available_spells("spells.json")
available_classes = load_available_classes("classes.json")
available_feats = load_available_feats("feats.json")
available_first_names = load_names("first-names.json")
available_middle_names = load_names("middle-names.json")
available_equipment = load_available_equipment("equipment.json")
