import re

summary = 0
data = []

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")
    data.append(line)

file.close()

# Definiálunk egy flag-et - ez jelzi hogy kell-e számolnunk vagy nem
do_it = True

for d in data:

    # Kiegészítjük az első regexet, úgy hogy a <do()> és a <don't()> utasításokat is felismerje
    x = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)", d)

    # Végigmegyünk a lista elemein amik vagy egy mul(<szám>,<szám>) vagy egy do() vagy don't() elemből állnak
    for match in x:

        # Ha do() vagy don't() átállítjuk a flaget ennek megfelőlen
        if match == "do()":
            do_it = True
        elif match == "don't()":
            do_it = False
        # Ha egy szorzás akkor a flag aktuális állapotának megfelelően vagy kiszámoljuk vagy nem csinálunk semmit
        else:
            if do_it:

                match = match[4:-1]

                numbers = match.split(",")

                summary = summary + (int(numbers[0]) * int(numbers[1]))

print("Summary:", summary)
