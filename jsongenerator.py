from json import dump

name_source = "rawnames.txt"
first = []
middle = []
last = []
with open(name_source, "r", encoding='utf-8') as f:
    for line in f:
        if len(line) == 0 or line[0] == '\n':
            continue
        line.replace('\n', '')
        words = line.split(' ')
        if(len(words) == 0):
            continue
        first.append(words[0])
        if(len(words) == 1):
            continue
        last.append(words[len(words) - 1])
        words = words[1:-1]
        middle.extend(words)

with open("first.json", "w") as f:
    dump(first, f)

with open("middle.json", "w") as f:
    dump(middle, f)

with open("last.json", "w") as f:
    dump(last, f)
