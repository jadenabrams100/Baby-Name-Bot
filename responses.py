from json import load, dump
from random import choice, choices

namesRepo = {}

def get_response(num_middle_names: int) -> str:
    first: str = choice(namesRepo["first"])
    first.rstrip('\n')
    first.strip()
    middle_names_list: list[str] = choices(namesRepo["middle"], k=num_middle_names)
    middle: str = " ".join(middle_names_list)
    last: str = choice(namesRepo["last"])
    last.rstrip('\n')
    last.strip()
    if len(middle_names_list) < 1:
        return first + " " + last
    return first + " " + middle + " " + last

def load_json() -> None:
    global namesRepo
    try:
        with open('first-test.json', 'r') as f:
            namesRepo["first"] = load(f)
        with open('middle-test.json', 'r') as f:
            namesRepo["middle"] = load(f)
        with open('last-test.json', 'r') as f:
            namesRepo["last"] = load(f)
    except Exception as e:
        print("Could not load json, see stack trace")
        print(e)