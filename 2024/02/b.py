import copy


def check_increasing(current_number, next_number, state):

    if not state:
        return False
    else:
        if (next_number - current_number) in [1, 2, 3]:
            return True
        else:
            return False


def check_decreasing(current_number, next_number, state):

    if not state:
        return False
    else:
        if (next_number - current_number) in [-1, -2, -3]:
            return True
        else:
            return False


data = []
safe_levels = []

f = open("input.txt", "r", encoding="utf-8")

for line in f:

    split = []
    line = line.rstrip("\n")
    temp = line.split(" ")

    for t in temp:
        split.append(int(t))

    data.append(split)

f.close()

for i in range(len(data)):

    safe = True

    if data[i][1] - data[i][0] < 0:
        for j in range(len(data[i]) - 1):
            safe = check_decreasing(data[i][j], data[i][j+1], safe)
    elif data[i][1] - data[i][0] > 0:
        for j in range(len(data[i]) - 1):
            safe = check_increasing(data[i][j], data[i][j+1], safe)
    else:
        safe = False

    if safe:
        safe_levels.append(i)

# Eddig a pontig megegysezik a feladat első részének megoldásával
# Annyi különbséggel, hogy nem számoljuk a megfelelő sorokat, hanem egy listába tesszük a sorszámaikat | safe_levels = []

# Mégegyszer végig megyünk az egész mátrixon
for i in range(len(data)):

    # Ha a sor nem volt megfelelő elsőre nézzük meg az engedménnyel
    if i not in safe_levels:

        # Bármelyik elemet kivehetjük a sorból -> végig megyünk a sor összes elemén
        for j in range(len(data[i])):

            # Optimistán feltesszük, hogy ha kiveszünk egy elemet akkor jó lesz a sor
            maybe_safe = True

            # Deep Copy-t csinálunk az adott sorról és ezzel a másolattal dolgozunk tovább, különben folyamatosan az "igazi"
            # sorból vennénk ki az elemeket
            temporary = copy.copy(data[i])

            # Kivesszük az adott elemet
            temporary.pop(j)

            # Ez ugyanaz mint az elős részben, csak most az egy elemmel csökkentett sort nézzük
            if temporary[1] - temporary[0] < 0:
                for m in range(len(temporary) - 1):
                    maybe_safe = check_decreasing(temporary[m], temporary[m+1], maybe_safe)
            elif temporary[1] - temporary[0] > 0:
                for m in range(len(temporary) - 1):
                    maybe_safe = check_increasing(temporary[m], temporary[m+1], maybe_safe)
            else:
                maybe_safe = False

            # Ha jó lett a sor akkor hozzáadjuk a sorszámát az első ellenőrzés során használt listához
            if maybe_safe:
                safe_levels.append(i)

# Egy kis csavar - Egy sort többször is hozzáaadhattunk a safe_levels lisáthoz, mert ha egy rossz sor megjavult,
# ha az első elemét vettük ki, illetve akkor is ha a negyediket akkor az első és negyedik alkalommal hozzáadtuk
# Ezért a safe_levels listából egy halmazt hozunk létre (kiszűri a duplikált sorszámokat) és ennek a halmaznak a számossága
# len(set(safe_levels) a megoldásunk
safe_levels_with_dampener = len(set(safe_levels))
print("Safe levels with dampener:", safe_levels_with_dampener)
