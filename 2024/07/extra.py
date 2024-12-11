# Érdekes hogy mennyivel gyorsabb ez a megoldás

# Gondolatmenet: Fordítsuk meg az egészet és az eredményből számoljunk visszafele
# Szorzás helyett osztunk - összeadás helyett kivonunk, ha az eredményből indulva megkapjuk az első számot a listában
# akkor boldogak vagyunk
# Mivel alapból balról jobbra kell kiértékelni a műveleteket nem pedig a műveleti sorrend szerint
# Ebből kiindulva ha visszafele számolunk és a jelenlegi eredmény nem osztható maradék nélkül a soron következő számmal
# akkor azt az ágat már menetközben levághatjuk

# Kiértékelő függvény
def evaluate_numbers(result, numbers):

    # Ha a számok listája már csak 1 elemű, nézzük meg, hogy az eredmény egyenlő-e az utolsó számmal
    # Ha igen akkor ez egy valid megoldás
    if len(numbers) == 1:
        if result == numbers[0]:
            return True
        else:
            return False

    # Ha nem egy elemű a számok listája akkor végezzük el az osztást és kivonást, vagy csak a kivonást a következő számmal
    # és rekurzívan értékeljük tovább az eredményt
    else:
        if int(result) % numbers[0] == 0:
            return evaluate_numbers(result - numbers[0], numbers[1:]) or evaluate_numbers(int(result / numbers[0]), numbers[1:])
        else:
            return evaluate_numbers(result - numbers[0], numbers[1:])


data = []

solution = 0

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")

    temp = line.split()[1:]
    k = []

    for t in temp:
        k.append(int(t))

    k.reverse()

    data.append([int(line.split(": ")[0]), k])

file.close()

for d in data:

    if evaluate_numbers(d[0], d[1]):
        solution = solution + d[0]

print("Solution:", solution)
