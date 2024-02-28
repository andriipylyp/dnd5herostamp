import random
from typing import Dict, Optional, Tuple, Union
import json
import attr

TRAITS_DATA_TYPE = Tuple[Dict[str, str], ...]
SPELL_CLASSES_DATA_TYPE = Tuple[str, ...]
SPELL_COMPONENTS_DATA_TYPE = Dict[str, Union[str, bool]]
SPELL_TAGS_DATA_TYPE = Tuple[str, ...]


@attr.frozen
class Race:
    name: str
    source: str
    size: str
    speed: int
    traits: TRAITS_DATA_TYPE
    str: int = 0
    dex: int = 0
    con: int = 0
    int: int = 0
    wis: int = 0
    cha: int = 0
    choose: int = 0

    def get_data(self) -> Dict:
        return attr.asdict(self)


@attr.frozen
class Spell:
    casting_time: str
    classes: SPELL_CLASSES_DATA_TYPE
    components: SPELL_COMPONENTS_DATA_TYPE
    description: str
    duration: str
    level: str
    higher_levels: str
    name: str
    range: str
    ritual: bool
    school: str
    tags: SPELL_TAGS_DATA_TYPE
    type: str


@attr.frozen
class Class:
    name: str
    str: bool
    dex: bool
    con: bool
    int: bool
    wis: bool
    cha: bool

    @property
    def weapon_proficiencies(self) -> Tuple[str, ...]:
        if self.name == "Bard" or self.name == "Rogue":
            return ("Simple Ranged Weapons", "Simple Melee Weapons", "Martial Melee Weapons")
        elif (
            self.name == "Barbarian"
            or self.name == "Warrior"
            or self.name == "Paladin"
            or self.name == "Ranger"
        ):
            return (
                "Simple Ranged Weapons",
                "Simple Melee Weapons",
                "Martial Melee Weapons",
                "Martial Ranged Weapons",
            )
        elif (
            self.name == "Wizard"
            or self.name == "Druid"
            or self.name == "Cleric"
            or self.name == "Warlock"
            or self.name == "Monk"
            or self.name == "Sorcerer"
        ):
            return ("Simple Ranged Weapons", "Simple Melee Weapons")

    @property
    def armor_proficiencies(self) -> Tuple[str, ...]:
        if self.name == "Bard" or self.name == "Warlock" or self.name == "Rogue":
            return ("Light Armor",)
        elif (
            self.name == "Barbarian" or self.name == "Druid" or self.name == "Cleric" or self.name == "Ranger"
        ):
            return ("Light Armor", "Medium Armor", "Shield")
        elif self.name == "Warrior" or self.name == "Paladin":
            return ("Light Armor", "Medium Armor", "Heavy Armor", "Shield")
        elif self.name == "Wizard" or self.name == "Monk" or self.name == "Sorcerer":
            return ()

    @property
    def has_cantrip(self) -> bool:
        if self.name in ["Wizard", "Warrior", "Sorcerer", "Druid", "Bard", "Cleric", "Warlock", "Rogue"]:
            return True
        return False

    @property
    def class_abilities(self):
        if self.name == "Wizard":
            return {
                1: [3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [3, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                4: [4, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                5: [4, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                6: [4, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                7: [4, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                8: [4, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                9: [4, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                10: [5, 4, 3, 3, 3, 2, 0, 0, 0, 0],
                11: [5, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                12: [5, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                13: [5, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                14: [5, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                15: [5, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                16: [5, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                17: [5, 4, 3, 3, 3, 2, 1, 1, 1, 1],
                18: [5, 4, 3, 3, 3, 3, 1, 1, 1, 1],
                19: [5, 4, 3, 3, 3, 3, 2, 1, 1, 1],
                20: [5, 4, 3, 3, 3, 3, 2, 2, 1, 1],
            }
        elif self.name == "Warrior":
            return {
                3: [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                4: [2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                5: [2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                6: [2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                7: [2, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                8: [2, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                9: [2, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                10: [3, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                11: [3, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                12: [3, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                13: [3, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                14: [3, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                15: [3, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                16: [3, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                17: [3, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                18: [3, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                19: [3, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                20: [3, 4, 3, 3, 1, 0, 0, 0, 0, 0],
            }
        elif self.name == "Bard":
            return {
                1: [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [2, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                4: [3, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                5: [3, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                6: [3, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                7: [3, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                8: [3, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                9: [3, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                10: [4, 4, 3, 3, 3, 2, 0, 0, 0, 0],
                11: [4, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                12: [4, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                13: [4, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                14: [4, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                15: [4, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                16: [4, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                17: [4, 4, 3, 3, 3, 2, 1, 1, 1, 1],
                18: [4, 4, 3, 3, 3, 3, 1, 1, 1, 1],
                19: [4, 4, 3, 3, 3, 3, 2, 1, 1, 1],
                20: [4, 4, 3, 3, 3, 3, 2, 2, 1, 1],
            }
        elif self.name == "Druid":
            return {
                1: [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [2, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                4: [3, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                5: [3, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                6: [3, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                7: [3, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                8: [3, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                9: [3, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                10: [4, 4, 3, 3, 3, 2, 0, 0, 0, 0],
                11: [4, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                12: [4, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                13: [4, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                14: [4, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                15: [4, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                16: [4, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                17: [4, 4, 3, 3, 3, 2, 1, 1, 1, 1],
                18: [4, 4, 3, 3, 3, 3, 1, 1, 1, 1],
                19: [4, 4, 3, 3, 3, 3, 2, 1, 1, 1],
                20: [4, 4, 3, 3, 3, 3, 2, 2, 1, 1],
            }
        elif self.name == "Cleric":
            return {
                1: [3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [3, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                4: [4, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                5: [4, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                6: [4, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                7: [4, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                8: [4, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                9: [4, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                10: [5, 4, 3, 3, 3, 2, 0, 0, 0, 0],
                11: [5, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                12: [5, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                13: [5, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                14: [5, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                15: [5, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                16: [5, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                17: [5, 4, 3, 3, 3, 2, 1, 1, 1, 1],
                18: [5, 4, 3, 3, 3, 3, 1, 1, 1, 1],
                19: [5, 4, 3, 3, 3, 3, 2, 1, 1, 1],
                20: [5, 4, 3, 3, 3, 3, 2, 2, 1, 1],
            }
        elif self.name == "Warlock":
            return {
                1: [2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                4: [3, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                5: [3, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                6: [3, 0, 0, 2, 0, 0, 0, 0, 0, 0],
                7: [3, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                8: [3, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                9: [3, 0, 0, 0, 0, 2, 0, 0, 0, 0],
                10: [4, 0, 0, 0, 0, 2, 0, 0, 0, 0],
                11: [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                12: [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                13: [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                14: [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                15: [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],
                16: [4, 0, 0, 0, 0, 4, 0, 0, 0, 0],
                17: [4, 0, 0, 0, 0, 4, 0, 0, 0, 0],
                18: [4, 0, 0, 0, 0, 4, 0, 0, 0, 0],
                19: [4, 0, 0, 0, 0, 4, 0, 0, 0, 0],
                20: [4, 0, 0, 0, 0, 4, 0, 0, 0, 0],
            }
        elif self.name == "Paladin":
            return {
                1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                4: [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                5: [0, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                6: [0, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                7: [0, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                8: [0, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                9: [0, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                10: [0, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                11: [0, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                12: [0, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                13: [0, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                14: [0, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                15: [0, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                16: [0, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                17: [0, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                18: [0, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                19: [0, 4, 3, 3, 3, 2, 0, 0, 0, 0],
                20: [0, 4, 3, 3, 3, 2, 0, 0, 0, 0],
            }
        elif self.name == "Rogue":
            return {
                1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [3, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                4: [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                5: [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                6: [3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                7: [3, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                8: [3, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                9: [3, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                10: [4, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                11: [4, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                12: [4, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                13: [4, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                14: [4, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                15: [4, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                16: [4, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                17: [4, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                18: [4, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                19: [4, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                20: [4, 4, 3, 3, 1, 0, 0, 0, 0, 0],
            }
        elif self.name == "Ranger":
            return {
                1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                4: [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                5: [0, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                6: [0, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                7: [0, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                8: [0, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                9: [0, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                10: [0, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                11: [0, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                12: [0, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                13: [0, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                14: [0, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                15: [0, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                16: [0, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                17: [0, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                18: [0, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                19: [0, 4, 3, 3, 3, 2, 0, 0, 0, 0],
                20: [0, 4, 3, 3, 3, 2, 0, 0, 0, 0],
            }
        elif self.name == "Sorcerer":
            return {
                1: [4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                2: [4, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                3: [4, 4, 2, 0, 0, 0, 0, 0, 0, 0],
                4: [5, 4, 3, 0, 0, 0, 0, 0, 0, 0],
                5: [5, 4, 3, 2, 0, 0, 0, 0, 0, 0],
                6: [5, 4, 3, 3, 0, 0, 0, 0, 0, 0],
                7: [5, 4, 3, 3, 1, 0, 0, 0, 0, 0],
                8: [5, 4, 3, 3, 2, 0, 0, 0, 0, 0],
                9: [5, 4, 3, 3, 3, 1, 0, 0, 0, 0],
                10: [6, 4, 3, 3, 3, 2, 0, 0, 0, 0],
                11: [6, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                12: [6, 4, 3, 3, 3, 2, 1, 0, 0, 0],
                13: [6, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                14: [6, 4, 3, 3, 3, 2, 1, 1, 0, 0],
                15: [6, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                16: [6, 4, 3, 3, 3, 2, 1, 1, 1, 0],
                17: [6, 4, 3, 3, 3, 2, 1, 1, 1, 1],
                18: [6, 4, 3, 3, 3, 3, 1, 1, 1, 1],
                19: [6, 4, 3, 3, 3, 3, 2, 1, 1, 1],
                20: [6, 4, 3, 3, 3, 3, 2, 2, 1, 1],
            }
        else:
            return {}


SHEET_SPELLS_DATA_TYPE = Tuple[Tuple[Spell, ...]]


@attr.frozen
class Subclass:
    name: str
    alignment: float  # -1 true evil, 1 true good
    spell_school: str = None
    notice: str = None
    caster: bool = False


SUBCLASSES = {
    "Barbarian": (
        Subclass("Berserk", -0.25),
        Subclass("Totem Warrior", 0.25),
        Subclass("Storm Herald", 0.5),
        Subclass("Ancestral Guardian", 0),
        Subclass("Zealot", -0.25),
        Subclass("Beast", 0, notice="Roll origin"),
        Subclass("Wild Magic", 0),
        Subclass("Giant", 0),
        Subclass("Battlerager", -0.25),
    ),
    "Bard": (
        Subclass("Valor", 0.5, spell_school="Random", caster=True),
        Subclass("Lore", 0, spell_school="Random", caster=True),
        Subclass("Swords", -0.25, spell_school="Transmutation", caster=True),
        Subclass("Glamour", 0, spell_school="Enchantment", caster=True),
        Subclass("Whispers", -0.6, spell_school="Illusion", caster=True),
        Subclass("Creation", 0, spell_school="Evocation", caster=True),
        Subclass("Eloquence", 0, spell_school="Enchantment", caster=True),
        Subclass("Spirits", 0, spell_school="Evocation", caster=True),
    ),
    "Warrior": (
        Subclass("Battle Master", 0, notice="Roll mastery"),
        Subclass("Eldritch Knight", 0, spell_school="Abjuration", caster=True),
        Subclass("Champion", 0),
        Subclass("Cavalier", 0),
        Subclass("Arcane Archer", 0, notice="Roll magic arrows"),
        Subclass("Samurai", 0),
        Subclass("Psi Warrior", 0),
        Subclass("Rune Knight", 0, notice="Roll rune mastery"),
        Subclass("Purple Dragon", 1),
        Subclass("Echo", 0),
    ),
    "Wizard": (
        Subclass("Evocation", 0, spell_school="Evocation", caster=True),
        Subclass("Conjuration", 0, spell_school="Conjuration", caster=True),
        Subclass("Illusion", 0, spell_school="Illusion", caster=True),
        Subclass("Necromancy", -1, spell_school="Necromancy", caster=True),
        Subclass("Abjuration", 0.5, spell_school="Abjuration", caster=True),
        Subclass("Enchantment", 0, spell_school="Enchantment", caster=True),
        Subclass("Transmutation", 0, spell_school="Transmutation", caster=True),
        Subclass("Divination", 0, spell_school="Divination", caster=True),
        Subclass("Warmage", 0, spell_school="Evocation", caster=True),
        Subclass("Bladesinging", -0.1, spell_school="Evocation", caster=True),
        Subclass("Scribes", 0, spell_school="Random", caster=True),
        Subclass("Bladesong", 0, spell_school="Evocation", caster=True),
        Subclass("Chronurgy", 0, spell_school="Random", caster=True),
        Subclass("Graviturgy", 0, spell_school="Random", caster=True),
    ),
    "Druid": (
        Subclass("Land", 0, spell_school="Random", caster=True, notice="Roll subclass spells"),
        Subclass("Moon", 0, spell_school="Random", caster=True, notice="Roll creature"),
        Subclass("Shepherd", 0.5, spell_school="Random", caster=True),
        Subclass("Dreams", 0.5, spell_school="Random", caster=True),
        Subclass("Spores", -0.5, spell_school="Random", caster=True),
        Subclass("Stars", 0, spell_school="Random", caster=True),
        Subclass("Wildfire", 0, spell_school="Transmutation", caster=True),
    ),
    "Cleric": (
        Subclass("Tempest", 0, spell_school="Evocation", caster=True),
        Subclass("War", -0.5, spell_school="Abjuration", caster=True),
        Subclass("Life", 1, spell_school="Evocation", caster=True),
        Subclass("Knowledge", 0, spell_school="Random", caster=True),
        Subclass("Trickery", -1, spell_school="Illusion", caster=True),
        Subclass("Nature", 0.3, spell_school="Transmutation", caster=True),
        Subclass("Light", 1, spell_school="Evocation", caster=True),
        Subclass("Forge", 0.5, spell_school="Transmutation", caster=True),
        Subclass("Grave", 1, spell_school="Necromancy", caster=True),
        Subclass("Death", -1, spell_school="Necromancy", caster=True),
        Subclass("Order", 0, spell_school="Enchantment", caster=True),
        Subclass("Peace", 1, spell_school="Enchantment", caster=True),
        Subclass("Twilight", 0.5, spell_school="Conjuration", caster=True),
        Subclass("Arcana", 0, spell_school="Divination", caster=True),
    ),
    # "Artificer": (
    #     Subclass("Alchemist", 0, spell_school="Transmutation", caster=True),
    #     Subclass("Artillerist", 0, spell_school="Evocation", caster=True),
    #     Subclass("Battle Smith", 0, spell_school="Abjuration", caster=True),
    #     Subclass("Armorer", 0, spell_school="Abjuration", caster=True),
    # ), # NOT IN SPELLBOOK
    "Warlock": (
        Subclass("Archfey", 0, spell_school="Random", caster=True),
        Subclass("Fiend", 0, spell_school="Random", caster=True),
        Subclass("Great Old One", 0, spell_school="Enchantment", caster=True),
        Subclass("Hexblade", 0, spell_school="Random", caster=True),
        Subclass("Celestial", 0, spell_school="Evocation", caster=True),
        Subclass("Fathomless", 0, spell_school="Evocation", caster=True),
        Subclass("Genie", 0, spell_school="Random", caster=True),
        Subclass("Undying", 0, spell_school="Necromancy", caster=True),
        Subclass("Undead", 0, spell_school="Necromancy", caster=True),
    ),
    "Monk": (
        Subclass("Open Hand", 0),
        Subclass("Shadow", -0.5),
        Subclass("Four Elements", 0, notice="Roll practice"),
        Subclass("Kensei", 0),
        Subclass("Drunken Master", 0),
        Subclass("Sun Soul", 0),
        Subclass("Mercy", 1),
        Subclass("Astral elf", 0),
        Subclass("Ascendant Dragon", 0, notice="Roll origin"),
        Subclass("Long Death", -1),
    ),
    "Paladin": (  # TODO: FIX CANTRIPS
        Subclass("Devotion", 1, spell_school="Abjuration", caster=True),
        Subclass("Ancients", 1, spell_school="Transmutation", caster=True),
        Subclass("Vengeance", 0, spell_school="Random", caster=True),
        Subclass("Redemption", 1, spell_school="Enchantment", caster=True),
        Subclass("Conquest", -1, spell_school="Enchantment", caster=True),
        Subclass("Oathbreaker", -1, spell_school="Random", caster=True),
        Subclass("Glory", 0, spell_school="Transmutation", caster=True),
        Subclass("Watchers", 1, spell_school="Divination", caster=True),
        Subclass("Crown", 1, spell_school="Enchantment", caster=True),
    ),
    "Rogue": (
        Subclass("Thief", -0.5),
        Subclass("Assasin", -0.5),
        Subclass("Arcane Trickster", 0, spell_school="Illusion", caster=True),
        Subclass("Swashbuckler", 0),
        Subclass("Mastermind", -0.5),
        Subclass("Scout", -0.5),
        Subclass("Unquisitive", 0.5),
        Subclass("Phantom", -0.8),
        Subclass("Soulknife", 0),
    ),
    "Ranger": (  # TODO: FIX CANTRIPS
        Subclass("Hunter", 0, spell_school="Random", caster=True),
        Subclass("Beast Master", 0, spell_school="Random", caster=True),
        Subclass("Horizon Walker", 0.5, spell_school="Abjuration", caster=True),
        Subclass("Gloom Stalker", -0.5, spell_school="Illusion", caster=True),
        Subclass("Monster Slayer", 0, spell_school="Abjuration", caster=True),
        Subclass("Fey Wanderer", 0.5, spell_school="Enchantment", caster=True),
        Subclass("Swarmkeeper", 0, spell_school="Evocation", caster=True),
        Subclass("Drakewarden", 0, spell_school="Random", caster=True, notice="Roll origin"),
    ),
    "Sorcerer": (
        Subclass("Draconic", 0, spell_school="Random", caster=True, notice="Roll origin"),
        Subclass("Wild Magic", 0, spell_school="Random", caster=True),
        Subclass("Divine Soul", 0, spell_school="Random", caster=True, notice="Roll origin"),
        Subclass("Shadow", -0.3, spell_school="Random", caster=True, notice="Roll origin"),
        Subclass("Storm", 0, spell_school="Random", caster=True),
        Subclass("Aberrant Mind", 0, spell_school="Random", caster=True, notice="Roll origin"),
        Subclass("Clockwork Soul", 0, spell_school="Random", caster=True, notice="Roll origin"),
    ),
}


@attr.frozen
class Item:
    name: str
    cost: str
    damage: Optional[str]
    cd: Optional[int]
    type: str


def generate_random_hp(base: int, con_mod: int, level: int) -> int:
    return sum([random.randint(1, base) + con_mod for _ in range(level - 1)]) + base + con_mod


@attr.frozen
class Sheet:
    level: int
    rating: str
    name: str
    race: Race
    cl: Class
    sub_cl: Subclass
    spells: SHEET_SPELLS_DATA_TYPE
    items: Tuple[Item, ...]
    base_str: int
    base_dex: int
    base_con: int
    base_wis: int
    base_int: int
    base_cha: int
    feats: Optional[Tuple] = None

    @property
    def hp(self):
        if self.cl.name == "Barbarian":
            return generate_random_hp(12, self.con_mod, self.level)
        elif (
            self.cl.name == "Bard"
            or self.cl.name == "Druid"
            or self.cl.name == "Cleric"
            or self.cl.name == "Warlock"
            or self.cl.name == "Monk"
            or self.cl.name == "Rogue"
        ):
            return generate_random_hp(8, self.con_mod, self.level)
        elif self.cl.name == "Warrior" or self.cl.name == "Paladin" or self.cl.name == "Ranger":
            return generate_random_hp(10, self.con_mod, self.level)
        elif self.cl.name == "Wizard" or self.cl.name == "Sorcerer":
            return generate_random_hp(6, self.con_mod, self.level)

    @property
    def bm(self):
        if self.level < 5:
            return 2
        elif self.level >= 5 and self.level < 9:
            return 3
        elif self.level >= 9 and self.level < 13:
            return 4
        elif self.level >= 13 and self.level < 17:
            return 5
        elif self.level >= 17:
            return 6

    @property
    def passive_perception(self):
        return 10 + self.wis_mod

    @property
    def str(self):
        return self.base_str + self.race.str

    @property
    def dex(self):
        return self.base_dex + self.race.dex

    @property
    def con(self):
        return self.base_con + self.race.con

    @property
    def wis(self):
        return self.base_wis + self.race.wis

    @property
    def int(self):
        return self.base_int + self.race.int

    @property
    def cha(self):
        return self.base_cha + self.race.cha

    @property
    def str_mod(self):
        return (self.str - 10) // 2

    @property
    def dex_mod(self):
        return (self.dex - 10) // 2

    @property
    def con_mod(self):
        return (self.con - 10) // 2

    @property
    def wis_mod(self):
        return (self.wis - 10) // 2

    @property
    def int_mod(self):
        return (self.int - 10) // 2

    @property
    def cha_mod(self):
        return (self.cha - 10) // 2


@attr.frozen
class Feat:
    name: str
    text: Tuple[str, ...]


def load_available_races(file: str) -> Tuple[Race, ...]:
    def get_abilities_from_text(text: str) -> Dict[str, Optional[int]]:
        abilities = {
            "Str": 0,
            "Dex": 0,
            "Con": 0,
            "Int": 0,
            "Wis": 0,
            "Cha": 0,
            "Choose": 0,
        }
        for ability in text.split(", "):
            ability_splited = ability.split(" ")
            abilities[ability_splited[0]] = int(ability_splited[1])
        return abilities.values()

    # Open the JSON file for reading
    with open(file, "r", encoding="utf8") as file:
        # Parse JSON file
        raw_races = json.load(file)
    available_races = []
    for race in raw_races["compendium"]["race"]:
        abilities = get_abilities_from_text(race["ability"])
        available_races.append(
            Race(
                race["name"],
                race["source"],
                race["size"],
                int(race["speed"]),
                tuple([{"name": t["name"], "text": t["text"]} for t in race["trait"]]),
                *abilities
            )
        )
    return tuple(available_races)


def load_available_spells(file: str) -> Tuple[Spell, ...]:
    def parse_higher_levels(spell: Dict) -> Dict:
        if "higher_levels" not in spell.keys():
            spell["higher_levels"] = None
        return spell

    with open(file, "r", encoding="utf8") as file:
        # Parse JSON file
        raw_spells = json.load(file)
    return tuple([Spell(**parse_higher_levels(spell)) for spell in raw_spells])


def load_available_classes(file: str) -> Tuple[Class, ...]:
    def get_proficiency_from_text(text: str) -> Dict[str, bool]:
        proficiency = {"str": False, "dex": False, "con": False, "int": False, "wis": False, "cha": False}
        mapping = {
            "Strength": "str",
            "Dexterity": "dex",
            "Constitution": "con",
            "Intelligence": "int",
            "Wisdom": "wis",
            "Charisma": "cha",
        }
        text_splitted = text.split(", ")
        for prof in text_splitted:
            proficiency[mapping[prof]] = True
        return proficiency

    with open(file, "r", encoding="utf8") as file:
        # Parse JSON file
        raw_classes = json.load(file)
    return tuple([Class(cl["name"], **get_proficiency_from_text(cl["proficiency"])) for cl in raw_classes])


def load_available_feats(file: str) -> Tuple[Feat, ...]:
    with open(file, "r", encoding="utf8") as file:
        # Parse JSON file
        raw_feats = json.load(file)
    return tuple([Feat(feat["name"], feat["text"]) for feat in raw_feats])


def load_names(file: str) -> Tuple[str, ...]:
    with open(file, "r", encoding="utf8") as file:
        # Parse JSON file
        raw_names = json.load(file)
    return tuple(raw_names)


def load_available_equipment(file: str) -> Tuple[Item, ...]:
    with open(file, "r", encoding="utf8") as file:
        # Parse JSON file
        raw_names = json.load(file)["Equipment"]
    available_light_armor = tuple(
        [
            Item(
                v,
                raw_names["Armor"]["Armor List"]["Light Armor"]["table"]["Cost"][i],
                None,
                raw_names["Armor"]["Armor List"]["Light Armor"]["table"]["Armor Class (AC)"][i],
                type="Light Armor",
            )
            for i, v in enumerate(raw_names["Armor"]["Armor List"]["Light Armor"]["table"]["Armor"])
        ]
    )
    available_medium_armor = tuple(
        [
            Item(
                v,
                raw_names["Armor"]["Armor List"]["Medium Armor"]["table"]["Cost"][i],
                None,
                raw_names["Armor"]["Armor List"]["Medium Armor"]["table"]["Armor Class (AC)"][i],
                type="Medium Armor",
            )
            for i, v in enumerate(raw_names["Armor"]["Armor List"]["Medium Armor"]["table"]["Armor"])
        ]
    )
    available_heavy_armor = tuple(
        [
            Item(
                v,
                raw_names["Armor"]["Armor List"]["Heavy Armor"]["table"]["Cost"][i],
                None,
                raw_names["Armor"]["Armor List"]["Heavy Armor"]["table"]["Armor Class (AC)"][i],
                type="Heavy Armor",
            )
            for i, v in enumerate(raw_names["Armor"]["Armor List"]["Heavy Armor"]["table"]["Armor"])
        ]
    )
    shield = (Item("Shield", "10 gp", None, cd="2", type="Shield"),)
    available_simple_melee_weapons = tuple(
        [
            Item(
                v,
                raw_names["Weapons"]["Weapons List"]["Simple Melee Weapons"]["table"]["Cost"][i],
                raw_names["Weapons"]["Weapons List"]["Simple Melee Weapons"]["table"]["Damage"][i],
                None,
                type="Simple Melee Weapons",
            )
            for i, v in enumerate(
                raw_names["Weapons"]["Weapons List"]["Simple Melee Weapons"]["table"]["Name"]
            )
        ]
    )
    available_simple_ranged_weapons = tuple(
        [
            Item(
                v,
                raw_names["Weapons"]["Weapons List"]["Simple Ranged Weapons"]["table"]["Cost"][i],
                raw_names["Weapons"]["Weapons List"]["Simple Ranged Weapons"]["table"]["Damage"][i],
                None,
                type="Simple Ranged Weapons",
            )
            for i, v in enumerate(
                raw_names["Weapons"]["Weapons List"]["Simple Ranged Weapons"]["table"]["Name"]
            )
        ]
    )
    available_simple_ranged_weapons = tuple(
        [
            Item(
                v,
                raw_names["Weapons"]["Weapons List"]["Simple Ranged Weapons"]["table"]["Cost"][i],
                raw_names["Weapons"]["Weapons List"]["Simple Ranged Weapons"]["table"]["Damage"][i],
                None,
                type="Simple Ranged Weapons",
            )
            for i, v in enumerate(
                raw_names["Weapons"]["Weapons List"]["Simple Ranged Weapons"]["table"]["Name"]
            )
        ]
    )
    available_martial_melee_weapons = tuple(
        [
            Item(
                v,
                raw_names["Weapons"]["Weapons List"]["Martial Melee Weapons"]["table"]["Cost"][i],
                raw_names["Weapons"]["Weapons List"]["Martial Melee Weapons"]["table"]["Damage"][i],
                None,
                type="Martial Melee Weapons",
            )
            for i, v in enumerate(
                raw_names["Weapons"]["Weapons List"]["Martial Melee Weapons"]["table"]["Name"]
            )
        ]
    )
    available_martial_ranged_weapons = tuple(
        [
            Item(
                v,
                raw_names["Weapons"]["Weapons List"]["Martial Ranged Weapons"]["table"]["Cost"][i],
                raw_names["Weapons"]["Weapons List"]["Martial Ranged Weapons"]["table"]["Damage"][i],
                None,
                type="Martial Ranged Weapons",
            )
            for i, v in enumerate(
                raw_names["Weapons"]["Weapons List"]["Martial Ranged Weapons"]["table"]["Name"]
            )
        ]
    )
    return (
        available_heavy_armor
        + available_light_armor
        + available_martial_melee_weapons
        + available_martial_ranged_weapons
        + available_medium_armor
        + available_simple_melee_weapons
        + available_simple_ranged_weapons
        + shield
    )
