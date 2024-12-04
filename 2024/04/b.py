# Röviden: "A" beűket kereseünk M-ekkel és S-ekkel körülírva.
# A szélső sorokat és oszlopokat nem nézzük, ha ezen kívül találunk "A"-t akkor nézzük meg hogy fenn áll-e valamelyik
# lehetőség

#   M-M     M-S     S-S     S-M
#   -A-     -A-     -A-     -A-
#   S-S     M-s     M-M     S-M

# Ezek ellenőrzése van lekódolva az alábbi függyvényben, ha a 4 közül valamelyik van akkor oké, ha nem akkor False

def check_surroundings(data, i, j):

    if data[i-1][j-1] == "M" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S" and data[i+1][j+1] == "S":
        return True

    elif data[i+1][j-1] == "M" and data[i+1][j+1] == "M" and data[i-1][j-1] == "S" and data[i-1][j+1] == "S":
        return True

    elif data[i-1][j-1] == "M" and data[i+1][j-1] == "M" and data[i-1][j+1] == "S" and data[i+1][j+1] == "S":
        return True

    elif data[i-1][j+1] == "M" and data[i+1][j+1] == "M" and data[i-1][j-1] == "S" and data[i+1][j-1] == "S":
        return True

    else:
        return False


matrix = []
found = 0

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")
    matrix.append(list(line))

file.close()

for x in range(1, len(matrix)-1):

    for y in range(1, len(matrix[x])-1):

        if matrix[x][y] == "A":

            if check_surroundings(matrix, x, y):
                found = found + 1

print("Found:", found)
