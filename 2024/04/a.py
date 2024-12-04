# Függcény: Megnézi, hogy egy string XMAS vagy visszafele olvasva XMAS (SAMX)
# Egy fokkal egszerűbb dolgunk van így mert nem kell "visszafele" bejárni a mátrixot
def check_string(temporary_string):

    if temporary_string == "XMAS" or temporary_string == "SAMX":
        return True
    else:
        return False

# Az adott pontból (i, j) vízszintesen jobbra összeolvasott négy karakter - madj ezt ellenőrizzük az előző függvénnyel
def check_horizontal(data, i, j):

    temporary_string = data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3]

    return check_string(temporary_string)

# Az adott pontból (i, j) függőlegesen összeolvasott négy karakter
def check_vertical(data, i, j):

    temporary_string = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]

    return check_string(temporary_string)


# Az adott pontból jobbra lefele összeolvasott négy karakter
def check_decreasing_diagonal(data, i, j):

    temporary_string = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]

    return check_string(temporary_string)

# Az adott pontból balre lefele összeolvasott négy karakter
def check_increasing_diagonal(data, i, j):

    temporary_string = data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3]

    return check_string(temporary_string)


matrix = []
found = 0

file = open("input.txt", "r", encoding="utf-8")

# Beolvassol a sorokat - mindegyik sort egy listává alakítjuk és hozzáfűzzük a matriy listához így kapjuk a mátrix
# reprezentációját az adatoknak
for line in file:

    line = line.rstrip("\n")
    matrix.append(list(line))

file.close()

# range függvény - A Python paraszt for ciklusa
# range függvény egy listát generál range(a, b, c) a-tól indulva, b-ig, c-kkel lépve
# range(0, 9, 2) => [0, 2, 4, 6, 8] - ezen lista elemein iterálunk végig

# Figyelnünk kell hogy ne indexeljünk túl - ezt figyelembe véve iterálunk a mátrix elemein
# Például amikor függőlegesen olvassuk a betűket akkor függőlegesen az alsó három sorba nem mehetünk mert onnan nincs
# negyedik karakter ezért range(len(matrix) - 3) => range(0, matrix hossza - 3, 1) "teljesen kiírva)
# x változó megy függőlegesen - y vízszintesen - Ezt mondjuk pont elcsesztem mint Gaben a napszemüveget


for x in range(len(matrix) - 3):

    for y in range(len(matrix[x]) - 3):

        if check_decreasing_diagonal(matrix, x, y):
            found = found + 1


for x in range(len(matrix) - 3):

    for y in range(3, len(matrix[x])):

        if check_increasing_diagonal(matrix, x, y):
            found = found + 1

for x in range(len(matrix)):

    for y in range(len(matrix[x]) - 3):

        if check_horizontal(matrix, x, y):
            found = found + 1

for x in range(len(matrix) - 3):

    for y in range(len(matrix[x])):

        if check_vertical(matrix, x, y):
            found = found + 1

print("Found:", found)
