# INFÓ: Eredetileg az extra.py lett volna a megoldásom egy nagyon szép rekurzív függvény
# Rosszul kezeltem le az inputot és azt hittem a gondolatmenetemmel van baj - eközben született
# ez a megoldás. Aztán rájöttem a hibára az első megoldásban, de a feladat második részére nem tudtam ráhúzni
# úgyhogy a második rész is ennek a brute-force megoldásnak a folytatása


# Függvény amivel az operations listába generáljuk a lehetséges műveleteket egy string formájában
# Első futásnál [] -> ["+", "*"]
# Második futásnál [] -> ["+", "*", "+*", "*+"]
# Majdnem mint egy hatványhalmaz
def generate_operations(operations):

    # Ha az operation lista üres akkor adjuk hozzá simán a két műveletet
    if len(operations) == 0:
        operations.append("+")
        operations.append("*")
    else:

        # Azért kell így külön ideiglenes listákba tenni mert ha a belső cikluson belül fűznénk hozzá, akkor
        # a ciklus végtelen lesz mert sose érünk a végére

        # A működés megértését a hallgatóra bízzuk, de vizsgán számon kérjük
        outer_temporary = []

        for o in operations:

            inner_temporary = ["+" + o, "*" + o]

            outer_temporary.extend(inner_temporary)

        operations.extend(outer_temporary)


data = []

solution = 0

file = open("input.txt", "r", encoding="utf-8")

# Gondolatmenet: Tároljuk a bemenő adatokat egy ilyen listában
# [[eredmény1, [számok1]], [eredmény2, [számok2], ... ]

# Az első megoldásban szótárban tároltam ahol az eredmények voltak a kulcsok, a sáémok pedig a kulcshoz
# tartozó értékek, csak az inputban egy eredmény többször előfordulhat, de kulcsként csak egyszer szerepelhet
# a szótárban és minden egyes alkalommal felülírodott a hozzá tartozó érték
for line in file:

    line = line.rstrip("\n")

    temp = line.split(" ")[1:]
    k = []

    for t in temp:
        k.append(int(t))

    data.append([int(line.split(": ")[0]), k])

file.close()

# Végigmegyünk az inputon
# d = [eredmény, [számok]]
# -> d[0] - eredmény
# -> d[1] - [számok] (lista)
# -> n = len(d[1])
for d in data:

    # Ebbe a listába generáljuk a műveleteket
    all_operations = []

    # Ide fogjuk kiszűrni az előző listából a megfelelő hosszú műveleteket
    # Ha n darab számot vizsgálunk n-1 darab művelet kell hozzá, az előző listában pedig benne vannak
    # a 0, 1, ..., k hosszú műveletek
    possible_operations = []

    # Boolean amivel jelezzük hogy az adott számokból előállítható e a művelet, ha már valahogy lehetséges az eredmény
    # nem kell tovább vizsgálni
    possible = False

    # Generáljuk le a lehetséges műveleteket n-1 hosszig
    for i in range(len(d[1]) - 1):
        generate_operations(all_operations)

    # Válasszuk ki közüllük a PONTOSAN n-1 hosszúakat
    for operation in all_operations:

        if len(operation) == len(d[1]) - 1:
            possible_operations.append(operation)

    # Menjünk végig a pontosan n-1 hosszú műveleteken
    for operation in possible_operations:

        # Ha még nem találtunk megoldást erre az inputra
        if not possible:

            # Az eredmény számolását kezdjük az első számmal a listából
            result = d[1][0]

            # A műveletek eddig stringként voltak ebből csináljunk listát
            # "+**+" -> ["+", "*", "*", "+"]
            operation_order = list(operation)

            # Végigmegyünk a műveletek az előbbi listából és annak megfelelően hozzádjuk a következő számot
            # vagy beszorzunk vele
            for i in range(len(operation_order)):

                if operation_order[i] == "*":
                    result = result * d[1][i+1]
                else:
                    result = result + d[1][i+1]

            # Ha az eredmény egyenlő azzal amit kerestünk akkor a possible flaget igazra állítjuk
            # ezzel jelezzük hogy mehetünk a következő sorra, nem kell tovább ezt vizságlni
            # Illetve a feladat megoldásához össze kell adni azokat az eredményeket amik lehetségesek
            if result == d[0]:
                possible = True
                solution = solution + d[0]

print("Solution:", solution)
