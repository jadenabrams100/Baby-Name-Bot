from json import load, dump
from random import choice, choices

namesRepo = {}

def get_name(num_middle_names: int) -> str:
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
        with open('first.json', 'r') as f:
            namesRepo["first"] = load(f)
        with open('middle.json', 'r') as f:
            namesRepo["middle"] = load(f)
        with open('last.json', 'r') as f:
            namesRepo["last"] = load(f)
    except Exception as e:
        print("Could not load json, see stack trace")
        print(e)

# gets multiple names in a row
# This function is responsible for handling if its own input is a number or not
# Return between one and twenty names
def multi_name(num_names) -> str:
    names = []
    try:
        num_names = int(num_names)
    except:
        #default to one name
        names.append("Unknown number, defaulting to one name.\n")
        num_names = 1
    # gate the amount of provided names to be between one and twenty
    num_names = max(1, min(num_names, 20))
    for x in range(num_names):
        names.append(get_name(1))
    # join name list together
    return '\n'.join(names)