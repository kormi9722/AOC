left_list = []
right_list = []

total_distance = 0

# Fájl megnyitása olvasásra
file = open("input.txt", "r", encoding="utf-8")

# Soronként végigmegyünk a fájlon
for line in file:

    # Eltávolítjuk a sor végéről (jobb oldaláról -> r(ight)strip) a newline karaktert
    line = line.rstrip("\n")

    # A sort "felvágjuk" a középén lévő három darab space mentén -> Két elemű listát kapunk ||| split = [egyik_szám, másik_szám]
    split = line.split("   ")

    # Az előbbi listából az első számot az egyik listába rakjuk, a másikat a másik listában
    # Integerré cast-oljuk a számot - stringként van beolvasva
    left_list.append(int(split[0]))
    right_list.append(int(split[1]))

# Fájl bezárása
file.close()

# HELYBEN rendezzük a két listát növekvő sorrendben
right_list.sort()
left_list.sort()

# Végigmegyünk a listákon (ugyanolyan hosszúak) és kiszámoljuk amit a lényeget
for i in range(len(left_list)):
    total_distance = total_distance + (abs(left_list[i] - right_list[i]))

print("Total distance:", total_distance)
