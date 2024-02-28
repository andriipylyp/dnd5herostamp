from typing import Tuple
from datamodel import Feat, Item, Race, Sheet, Class, SUBCLASSES, Subclass, Spell
from scipy.stats import norm
import random


def generate_level() -> Tuple[str, int]:
    probabilities = [
        57.9887,
        23.1955,
        11.5977,
        2.8994,
        1.2886,
        0.8284,
        0.5272,
        0.3222,
        0.2521,
        0.2000,
        0.1487,
        0.1160,
        0.0983,
        0.0805,
        0.0690,
        0.0580,
        0.0504,
        0.0446,
        0.0387,
        0.0322,
        0.0290,
        0.0264,
        0.0232,
        0.0176,
        0.0141,
        0.0116,
        0.0094,
        0.0077,
        0.0064,
        0.0055,
        0.0048,
        0.0043,
        0.0037,
    ]
    total = sum(probabilities)
    normalized_probabilities = [p / total for p in probabilities]
    ratings = [
        "0",
        "1/8",
        "1/4",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
    ]
    generated_rating = random.choices(ratings, weights=normalized_probabilities, k=1)[0]
    level = (
        list(range(1, 21))[ratings.index(generated_rating)] if ratings.index(generated_rating) <= 20 else 20
    )
    return generated_rating, level


def select_spell_by_class(
    cl_name: str, preferred_school: str, spell_list: Tuple[int, ...], available_spells: Tuple[Spell, ...],
):
    spells = []
    for spell_level in spell_list:
        if spell_level > 0:
            buffer_spells = []
            while len(buffer_spells) + 1 <= spell_level:
                names_in_buffer = [spell.name for spell in buffer_spells]
                if not spells:
                    selected_spells = [
                        spell
                        for spell in available_spells
                        if cl_name.lower() in spell.classes
                        and spell.level == "cantrip"
                        and spell.name not in names_in_buffer
                    ]
                else:
                    selected_spells = [
                        spell
                        for spell in available_spells
                        if cl_name.lower() in spell.classes
                        and spell.level != "cantrip"
                        and int(spell.level) == len(spells)
                        and spell.name not in names_in_buffer
                    ]

                if preferred_school == "Random":
                    buffer_spells.append(random.choice(selected_spells))
                elif random.random() >= 0.5:
                    selected_spells = [
                        spell for spell in selected_spells if spell.school == preferred_school.lower()
                    ]
                    if not selected_spells:
                        continue
                    buffer_spells.append(random.choice(selected_spells))
                else:
                    selected_spells = [
                        spell for spell in selected_spells if spell.school != preferred_school.lower()
                    ]
                    if not selected_spells:
                        continue
                    buffer_spells.append(random.choice(selected_spells))
            spells.append(buffer_spells.copy())
        else:
            spells.append([])
    return spells


def select_subclass_by_normal_distribution_of_alignment(
    alignment: float, subclasses: Tuple[Subclass, ...], scale: float = 0.5
) -> Subclass:
    weights = [norm.pdf(subclass.alignment, loc=alignment, scale=scale) for subclass in subclasses]
    return random.choices(subclasses, weights, k=1)[0]


def generate_character_name(
    available_first_names: Tuple[str, ...], available_middle_names: Tuple[str, ...]
) -> str:
    return random.choice(available_first_names) + " " + random.choice(available_middle_names)


def generate_random_base_stats(s: bool, d: bool, c: bool, w: bool, i: bool, ch: bool):
    def generate_attribute():
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])

    def sort_rolls_with_priorities(rolls, priorities):
        def find_two_largest_numbers_with_indices(lst):
            if len(lst) < 2:
                return "List needs to have at least two elements"

            # Find the indices of the two largest numbers
            largest_index = lst.index(max(lst))
            second_largest = min(lst)  # Initialize with the smallest value
            second_largest_index = None

            for i, num in enumerate(lst):
                if i != largest_index and num > second_largest:
                    second_largest_index = i
                    second_largest = num

            return (largest_index, lst[largest_index]), (second_largest_index, lst[second_largest_index])

        indexes = [i for i, value in enumerate(priorities) if value]
        buff = [v for i, v in enumerate(rolls) if i in indexes]
        m1, m2 = find_two_largest_numbers_with_indices(rolls)

        # Создание нового списка с учётом приоритетов
        sorted_rolls = rolls.copy()
        for i in indexes:
            if not buff or rolls[i] in buff:
                sorted_rolls[i] = m1[1] if rolls[i] != m1[1] else m2[1]
            else:
                sorted_rolls[i] = buff.pop(0)
        return sorted_rolls

    rolls = [generate_attribute() for _ in range(6)]
    priorities = [s, d, c, w, i, ch]
    sorted_attributes = sort_rolls_with_priorities(rolls, priorities)
    return sorted_attributes


def generate_random_equipment(
    armor_proficiencies: Tuple[str, ...],
    weapon_proficiencies: Tuple[str, ...],
    available_equipment: Tuple[Item, ...],
) -> Tuple[Item, ...]:
    if armor_proficiencies:
        selected_armor = [item for item in available_equipment if item.type in armor_proficiencies and item.type != "Shield"]
    else:
        selected_armor = [[]]
    selected_weapons = [item for item in available_equipment if item.type in weapon_proficiencies]
    return (random.choice(selected_armor), random.choice(selected_weapons), Item("Shield", "10 gp", None, None, "Shield") if (random.random() > 0.5 and "Shield" in armor_proficiencies) else None)


def generate_character(
    level: int,
    rating: str,
    available_first_names: Tuple[str, ...],
    available_middle_names: Tuple[str, ...],
    available_equipment: Tuple[Item, ...],
    available_races: Tuple[Race, ...],
    available_classes: Tuple[Class, ...],
    available_spells: Tuple[Spell, ...],
    available_feats: Tuple[Feat, ...],
    alignment: float = 0.0,
) -> Sheet:
    cl = random.choice(available_classes)
    sub_cl = select_subclass_by_normal_distribution_of_alignment(alignment, SUBCLASSES[cl.name])
    name = generate_character_name(available_first_names, available_middle_names)
    stats = generate_random_base_stats(cl.str, cl.dex, cl.con, cl.wis, cl.int, cl.cha)
    items = generate_random_equipment(cl.armor_proficiencies, cl.weapon_proficiencies, available_equipment)
    character_sheet = Sheet(
        level=level,
        rating=rating,
        name=name,
        race=random.choice(available_races),
        cl=cl,
        sub_cl=sub_cl,
        spells=None
        if not sub_cl.caster
        else select_spell_by_class(cl.name, sub_cl.spell_school, cl.class_abilities[level], available_spells),
        items=items,
        base_str=stats[0],
        base_dex=stats[1],
        base_con=stats[2],
        base_wis=stats[3],
        base_int=stats[4],
        base_cha=stats[5],
        feats=(random.choice(available_feats),),
    )
    return character_sheet
