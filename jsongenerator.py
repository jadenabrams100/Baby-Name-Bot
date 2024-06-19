from json import dump

first = []
middle = []
last = []
with open("rawnames.txt", "r") as f:
    for line in f:
        if len(line) == 0 or line[0] == '\n':
            continue
        line.replace("\n", "")
        words = line.split(' ')
        if(len(words) == 0):
            continue
        first.append(words[0])
        last.append(words[len(words) - 1])
        words = words[1:-1]
        middle.extend(words)

with open("first-test.json", "w") as f:
    dump(first, f)

with open("middle-test.json", "w") as f:
    dump(middle, f)

with open("last-test.json", "w") as f:
    dump(last, f)
