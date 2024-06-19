from json import load, dump
from random import choice, choices

namesRepo = {}

def get_response(num_middle_names: int) -> str:
    first: str = choice(namesRepo["first"])
    middle_names_list: list[str] = choices(namesRepo["middle"], k=num_middle_names)
    middle: str = " ".join(middle_names_list)
    last: str = choice(namesRepo["last"])
    return first + " " + middle + " " + last

def load_json() -> None:
    with open('names.json', 'r') as f:
        global namesRepo
        namesRepo = load(f)