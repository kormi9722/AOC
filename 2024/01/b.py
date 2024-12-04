left_list = []
right_list = []

similarity_score = 0

f = open("input.txt", "r", encoding="utf-8")

for line in f:

    line = line.rstrip("\n")
    split = line.split("   ")

    left_list.append(int(split[0]))
    right_list.append(int(split[1]))

f.close()

# Végigmegyünk a baloldali listán - count függvénnyel megszámoljuk hánszor fordul elő az aktuális szám a jobboldali listában
for i in range(len(left_list)):

    similarity_score = similarity_score + (left_list[i] * right_list.count(left_list[i]))

print("Similarity score:", similarity_score)
