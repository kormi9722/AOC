import re

result = 0
data = []

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")
    data.append(line)

file.close()

for d in data:

    # Írunk egy regexet és megkapjuk a "lényeget" egy listában
    x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", d)

    # Végigmegyünk az előbb kapott listán
    for match in x:

        # Így néznek ki a lista elemei mul(<szám>, <szám>)
        # Levágjuk az első négy és az utolsó karaktert -> <szám>,<szám>
        match = match[4:-1]

        # A mardékot a vesszőnél elválasztjuk
        numbers = match.split(",")

        # A két számot intergerré alakítjuk és elvégezzük a feladat által kért műveletet
        result = result + (int(numbers[0]) * int(numbers[1]))

print("Result:", result)
