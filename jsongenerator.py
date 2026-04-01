from json import dump

name_source = "SUPERIORNAMES.txt"
first = []
middle = []
last = []
with open(name_source, "r", encoding='utf-8') as f:
    for line in f:
        if len(line) == 0 or line[0] == '\n':
            continue
        # get rid of newline characters
        line = line.replace('\n', '')
        # split into individual names
        words = line.split(' ')
        #skip blanks
        if(len(words) == 0):
            continue
        # log first names
        first.append(words[0])
        # if we are done, go to the next thing
        if(len(words) == 1):
            continue
        # add last name
        last.append(words[len(words) - 1])
        # truncate to middle names
        words = words[1:-1]
        # move on if no middle names
        if(len(words) == 0):
            continue
        # add middle names
        middle.extend(words)

# export name lists
with open("first.json", "w") as f:
    dump(first, f)

with open("middle.json", "w") as f:
    dump(middle, f)

with open("last.json", "w") as f:
    dump(last, f)
