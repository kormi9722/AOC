import math

instructions = []

pages = []

result = 0

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")

    if "|" in line:

        temporary_split = line.split("|")
        instructions.append([int(temporary_split[0]), int(temporary_split[1]), False, False])

    elif "," in line:

        temporary_list = []
        temporary_split = line.split(",")

        for ts in temporary_split:

            temporary_list.append(int(ts))

        pages.append(temporary_list)

    else:
        pass

file.close()

for p in pages:

    for i in instructions:
        i[2] = False
        i[3] = False

    for i in instructions:

        if i[0] in p and i[1] in p:

            i[2] = True

    for i in instructions:

        if i[2]:

            first_index = p.index(i[0])
            second_index = p.index(i[1])

            if first_index < second_index:
                i[3] = True

    correct_order = True

    for i in instructions:

        if i[2]:

            if correct_order:

                if not i[3]:
                    correct_order = False

    # Eddig minden ugyanaz mint az első részben - viszont innen már azokkal a p-kkel foglalkozunk amik rossz sorrendben
    # vannak nyomtatva - sorrendbe kell tenni őket és utána megkeresni a középső oldalt

    # Egy gyors ábra a magyarázathoz: (Mindjárt kifejtem)
    # p             = [61, 13, 29]
    # page_ordering = [0, 0, 0]

    # Ha az adott p nincs jó sorrendben
    if not correct_order:

        # Létrehozunk egy nullákból álló listát annyi nullával ahány oldalszám van p-ben
        page_ordering = [0] * len(p)

        # Végigmegyünk az oldalszámokon az adott p-ben
        for page in p:

            # Minden oldalszámot összevetünk minden egyes nyomtatási instrukcióval [a, b, True, True/False]
            # Az utolsó True/False érték most nem érdekel minket
            for i in instructions:

                # Ez ugye azt jelenti hogy az adott instrukcióban lévő mindkét oldalszám benne van p-ben, tehát
                # releváns számunkra
                if i[2]:

                    # Tudjuk, hogy a és b is benne van az adott p-ben
                    # a az instrukció lista nulladik eleme -> a = i[0]
                    # b az instrukció lista első eleme -> b = i[1]

                    # Tudjuk, hogy b-t a után kell nyomtatni - igazából mindegy, hogy az adott instrukció
                    # listában mi az "a", az a lényeg hogy b-t "valami" után kell nyomtatni

                    # Ezért a page_ordering listában a b szám pozíciójában lévő nullát megnöveljük eggyel
                    # Így a végén a page_ordering listában meg kapjuk hogy az adott oldal hány másik oldal után kell
                    # hogy nyomtatva legyen

                    # p             = [61, 13, 29]
                    # page_ordering = [0, 6, 3]

                    # Itt a page_ordering lista elemeit el kéne osztani p hosszával mert így többször lett számolva minden
                    # De az eredményen nem változtat

                    # 61-es oldal 0 darab oldal után jön -> őt nyomtatjuk először
                    # 13-as oldal 6 darab oldal után jön -> őt nyomtatjuk utoljára
                    # ...

                    page_ordering[p.index(i[1])] = page_ordering[p.index(i[1])] + 1

        # Egy mátrix amiben összefűzöm p elemeit és a page_ordering lista elemeit - egymásnak megfelelően
        # ordering_matrix = [[0, 61], [6, 13], [3, 29]
        ordering_matrix = []

        for c in range(len(p)):
            ordering_matrix.append([page_ordering[c], p[c]])

        # Stackoverflow code: Listák listájának rendezése
        sorted_matrix = sorted(ordering_matrix, key=lambda x: x[0])

        # Megkeressük a középső lista sorszámát -> [rendezési segédszám, oldalszám]
        find_index = math.floor(len(sorted_matrix) / 2)
        # És az eredményhez adjuk a az oldalszámot belőle (egyes indexű elem)
        result = result + sorted_matrix[find_index][1]

print("Result:", result)
