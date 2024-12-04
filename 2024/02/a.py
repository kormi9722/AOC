# Függvény definíciók: A feladatban azt kell vizsgálni, hogy egy listában az egymást követő számok különbsége
# végig 1, 2 vagy 3 (-1, -2, 3)

# Ha a két szám különbsége az adott tartományban van akkor return True
# Ha a tartományon kívül van vagy már korábban nem volt megfelelő akkor return False
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


# data - Listák listája (mátrix)
data = []
safe_levels = 0

f = open("input.txt", "r", encoding="utf-8")

# Beolvassuk a sorokat... Minden sorhoz létrehozunk egy üres listát (split = []) ebben lesznek az integerek
# A sorokat felvágjuk space-enként kapunk egy temporary listát... Ezen végigmegyünk és int-té alakítjuk a stringként beolvastott számokat
# Az átalakított számokat hozzárakjuk a split listához
# Majd a split listát hozzá rakjuk a data listához
for line in f:

    split = []
    line = line.rstrip("\n")
    temporary = line.split(" ")

    for t in temporary:
        split.append(int(t))

    data.append(split)

f.close()

# Végigmegynk a mátrix sorain
for i in range(len(data)):

    # Minden sor elején feltesszük optimistán, hogy az adott sor megfelelő
    safe = True

    # Megnézzük, hogy a második szám kisebb / nagyobb / egyenlő e az elsőhöz képest
    # Ha kisebb / nagyobb akkor az összes többinek is kisebbnek / nagyobbnak kell lennie - ezalapján választjuk ki hogy melyik
    # függyvénnyel vizsgáljuk a sort
    # Ha a két szám egyenlő akkor már rossz
    if data[i][1] - data[i][0] < 0:

        # Végigmegyünk az adott soron (az utolsó előtti elemig iterálunk, hogy ne legyen túlindexelés)
        for j in range(len(data[i]) - 1):
            safe = check_decreasing(data[i][j], data[i][j+1], safe)
    elif data[i][1] - data[i][0] > 0:
        for j in range(len(data[i]) - 1):
            safe = check_increasing(data[i][j], data[i][j+1], safe)
    else:
        safe = False

    # Ha azután is megfelelő az adat miután végignéztük az adott sort akkor boldogak vagyunk
    if safe:
        safe_levels = safe_levels + 1

print("Safe levels:", safe_levels)


