import copy

# Ezt "sajnos" brute-force-oltam elvileg elég lenne megvizsgálni azokat a mezőket ahol a feladat első részében jártunk
# 1-2 perc a futásidő
# De ez valamiért nem működik, úgyhogy lehet van valami hiba a gondolatmenetemben

# Megoldás gondolatmenete: Az a feladat hogy ha egy mezőre akadályt teszünk akkor loop-ba kerül e az őr
# Ehhez az kell, hogy az őr úgy érkezzen egy mezőre ahol már korábban járt és ugyanolyan irányba ment tovább


lab_map = []

# Ebben számoljuk össze hány loop-ot tudunk összehozni
loop_counter = 0

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")
    lab_map.append(list(line))

file.close()

starting_position = [0, 0]

# Megkeressük az induló állását az őrnek
for i in range(len(lab_map)):
    for j in range(len(lab_map[i])):

        if lab_map[i][j] == "^":

            starting_position = [i, j]

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
starting_direction = 0

# Végigiterálunk az összes mezőn
for i in range(len(lab_map)):
    for j in range(len(lab_map[i])):

        # Reseteljük a jelenlegi pozíciót a kezdő pozícióra - és az irányt is
        current_position = copy.copy(starting_position)
        current_direction = 0

        # Létrehozunk egy halmazt - eben fogjuk tárolni hogy az őr melyik mezőn milyen irányba ment egy 3 elemű halmazként
        # steps = ((y1, x1, 1), (y2, x1, 1), ... )

        # Kezdetben üres ez a halmaz
        steps = set()

        # Loopban van-e az őr
        is_loop = False

        # Ha a jelenlegi mező nem "#" mivel ezt átállítani redundáns lenne és nem a "^" kezdőpozíció - oda nem rakhatunk
        # akadályt
        if lab_map[i][j] != "#" and lab_map[i][j] != "^":

            # Állítsuk át a mezőt "#" akadályra
            lab_map[i][j] = "#"

            # Hasonló mód mint a feladat első részében indítsuk el az őrt - két eshetőség lehet
            # Vagy kijön valamikor a térképből vagy loopba kerül
            while (-1 < current_position[0] < len(lab_map)) and (-1 < current_position[1] < len(lab_map[0])) and not is_loop:

                if lab_map[current_position[0]][current_position[1]] == "#":

                    current_position[0] = current_position[0] + (directions[current_direction][0] * -1)
                    current_position[1] = current_position[1] + (directions[current_direction][1] * -1)

                    current_direction = current_direction + 1

                    if current_direction == 4:
                        current_direction = 0

                else:

                    # Ha nem "#" akadály a jelenlegi pozició adjuk hozzá a halmazhoz az iránnyal együtt, ha még nincs
                    # benne a halmazban a jelenlegi pozíciót leitó halmaz (y, x, irány)
                    # Python Nerd Fact: Halmazba, csak hashelhető elemeket lehet tenni és a lista nem hashelhető
                    # ezért hazsnálunk halmazt a halmazban
                    if (current_position[0], current_position[1], current_direction) not in steps:
                        steps.add((current_position[0], current_position[1], current_direction))
                    # ha már benne van az (y, x, irány) halmaz akkor az őr már egy meglátgatott mezőn van és ugyanabba
                    # az irányba megy tovább -> loopba került
                    else:
                        is_loop = True

                current_position[0] = current_position[0] + directions[current_direction][0]
                current_position[1] = current_position[1] + directions[current_direction][1]

            # Ha úgy jöttünk ki az előző while ciklusból hogy loopba van az őr akkor számoljuk bele a megoldásba
            if is_loop:
                loop_counter = loop_counter + 1

            # Állítsuk vissza a térképet az eredeti állapotába
            lab_map[i][j] = "."

print("Number of possible loops:", loop_counter)
