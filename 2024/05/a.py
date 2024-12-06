import math

# Ebben tároljuk a nyomtatási utasításkat - Négy elemű listák listája
# [[a, b, False, False], [c, d, False, False] -> a-t hamrabb kell nyomtatni mint b-t
# Az inputból csak az első két számot kapjuk a két False-t már én fűzöm hozzá a megoldás szempontjából
# később kifejtem
instructions = []

# Ebben tároljuk a nyomtatandó oldalakot - N elemű listák listája
pages = []

# Ebben számoljuk az összeget amit a feladat kér
result = 0

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")

    # Ha az aktuális sorban benne van a | karakter akkoz egy nyomtatási utasítás
    # Elválasztjuk a 2 számot a | karakternél - kapunk egy ideiglenes két elemű listát
    # Az instruction listához hozzáfűzünk egy listát (az append függvényen belül hozzuk létre)
    # Ennek a listának az első két eleme a két szám (integerré castolva) az ideiglenes listából illetve még két False érték
    if "|" in line:

        temporary_split = line.split("|")
        instructions.append([int(temporary_split[0]), int(temporary_split[1]), False, False])

    # Ha az aktuális sorban , karakter van akkor az a nyomtatandó oldalak sorszámai
    # Az adott sort splitteljük egy ideiglenes listába a , karaktereknél
    # Majd egy násik ideiglenes listához adjuk őket integerré castolva és ezt a listát adjuk hozzá a pages listához
    elif "," in line:

        temporary_list = []
        temporary_split = line.split(",")

        for ts in temporary_split:

            temporary_list.append(int(ts))

        pages.append(temporary_list)

    # Ha se , se | ne csináljunk semmit
    else:
        pass

file.close()

# Végig megyünk a pages listák listáján - p változó is egy lista [1, 4, 23, 53] -> nyomtatandó oldalak (továbbiakban p)
for p in pages:

    # Ez az első iteráció során redundáns, minden iterációt tiszta lappal [a, b, False, False]-al akarunk kezdeni
    # Egy iteráció során változnak ezek az értékek itt reseteljük őket
    # Végig megyünk az instruction lista listáin és a lista második és harmadik elemét (Az alapból két False)
    # értéket False-ra állítjuk
    for i in instructions:
        i[2] = False
        i[3] = False

    # Megnézzük melyik instrukciókat kell figyelembe vennünk az adott oldalak nyomtatása során
    # A reset után ismét végig megyünk az instruction lista listáin - [a, b, False, False]
    # Ha a és b is benne van az adott p listában akkor az adott instrukcióban az első False-ot True-ra állítjuk
    for i in instructions:
        if i[0] in p and i[1] in p:
            i[2] = True

    # Ismét végigmegyünk az instruction lista listáin - most már csak azokat nézzük amik
    # ilyen alakúak -> [a, b, True, False] --- 72. sor if elágazás
    for i in instructions:

        if i[2]:

            # Megnézzük, hogy az adott instrukcióban szerepló számok a és b milyen sorszámmal szerepelnek p-ben
            # Pl: [0, 43, 2, a, 69, b, 89]
            # A példában first_index = 3 a second_index = 5
            first_index = p.index(i[0])
            second_index = p.index(i[1])

            # Ha a first_index kisebb mint a second_index akkor a két oldal az instrukciónak megfelelően van nyomtatva
            # És a második False-t True-ra állítjuk
            if first_index < second_index:
                i[3] = True

    # Optimistán feltesszük hogy az adott oldalak p-ben jó sorrendben vannak nyomtatva
    correct_order = True

    # Ismét végigmegyünk az instruction lista listáin - itt azt nézzük hogy egy instrukción belül ha az első
    # True/False érték True akkor a másik érték is True
    for i in instructions:

        # Ha az első True/False True
        if i[2]:

            # Ha még nem volt olyan oldal ami rossz sorrendben volt nyomtatva
            if correct_order:

                # Ha második True/False érték False akkor rossz sorrendben vannak nyomtatva az oldalak
                if not i[3]:
                    correct_order = False

    # Ha még mindig igaz a correct_order változó akkor az összes oldal jó sorrendben lett nyomtatva p-ben
    # Megkeressük a középső oldalszám sorszámát [index] és hozzáadjuk a result-hoz
    if correct_order:

        index = math.floor(len(p) / 2)

        result = result + p[index]

print("Result:", result)
