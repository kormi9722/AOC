# Listák listája - mátrix - ez lesz a térkép
lab_map = []

# Ebben számoljuk össze hány különböző korodinátán voltunk
positions_visited = 0

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")
    lab_map.append(list(line))

file.close()

# Csak adni kell neki valami kamu értéket mert ha if-en belül hozol létre egy változót akkor az IDE sír, hogy nem
# biztos hogy teljeseül
# Két elemű lista - [y, x] koordináták
current_position = [0, 0]

# Megkeressük a ^ karaktert ez lesz a kiindulási pont
for i in range(len(lab_map)):
    for j in range(len(lab_map[i])):

        if lab_map[i][j] == "^":

            current_position = [i, j]

# Egy listában felsoroljuk az irányvektorokat olyan sorrendben, hogy mindig egyet jobbra fordulunk
# [Fel, Jobbra, Le, Balra]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# Mivel felfele van a kezdő irány ez a 0. elem az előbbi listában - úgy tuudnk jobbra fordulni, ha ezt növeljük eggyel
# Ha eléri az érték a 4-et akkor visszaállítjuk 0-ra
current_direction = 0

# Az a cél hogy "kijöjjünk" a térképből - ezért amíg mindkét koordináta a térképen belül van addig "számolunk" tovább
while (-1 < current_position[0] < len(lab_map)) and (-1 < current_position[1] < len(lab_map[0])):

    # Ha a jelenlegi koordinátán "#" karakter van akkor lépjünk egyet vissza és forduljunk el jobbra
    # Meglehetett volna csinálni úgyis hogy előre megnézzük mi a következő mező de így egyszerűbb volt nekem
    if lab_map[current_position[0]][current_position[1]] == "#":

        # Visszalépünk egyet
        current_position[0] = current_position[0] + (directions[current_direction][0] * -1)
        current_position[1] = current_position[1] + (directions[current_direction][1] * -1)

        # Elfordulunk jobbra
        current_direction = current_direction + 1

        # Ha az érték 4 akkor legyen 0
        if current_direction == 4:
            current_direction = 0

    # Ha nem "#" a karakter (nem kell különbéseget tenni mostmár a "." és "^" között akkor írjuk át a karaktert
    # ezen a koordinátán valami másra - Például 0-ra
    else:

        lab_map[current_position[0]][current_position[1]] = "O"

    # Lépünk egyet előre
    current_position[0] = current_position[0] + directions[current_direction][0]
    current_position[1] = current_position[1] + directions[current_direction][1]

# Miután kijöttünk a térképről számoljuk össze hány koordinátán van 0 - ez lesz a megoldásunk
for i in range(len(lab_map)):
    for j in range(len(lab_map[i])):
        if lab_map[i][j] == "O":
            positions_visited = positions_visited + 1

print("Number of distinct positions visited:", positions_visited)
