# A megoldás menete teljesen ugyanaz mint az első részben csak 2 művelet helyett hármat kell megnézni
# Outputon, hogy hol tart a program :)

def generate_operations(operations):

    if len(operations) == 0:
        operations.append("+")
        operations.append("*")
        operations.append("|")
    else:

        outer_temporary = []

        for o in operations:

            inner_temporary = ["+" + o, "*" + o, "|" + o]

            outer_temporary.extend(inner_temporary)

        operations.extend(outer_temporary)


data = []

solution = 0

file = open("input.txt", "r", encoding="utf-8")

for line in file:

    line = line.rstrip("\n")

    temp = line.split()[1:]
    k = []

    for t in temp:
        k.append(int(t))

    data.append([int(line.split(": ")[0]), k])

file.close()

progress = 0

for d in data:

    progress = progress + 1
    print(progress, "/", len(data))

    all_operations = []
    possible_operations = []

    possible = False

    for i in range(len(d[1]) - 1):
        generate_operations(all_operations)

    for operation in all_operations:

        if len(operation) == len(d[1]) - 1:
            possible_operations.append(operation)

    for operation in possible_operations:

        if not possible:

            result = d[1][0]

            operation_order = list(operation)

            for i in range(len(operation_order)):

                if operation_order[i] == "*":
                    result = result * d[1][i+1]
                elif operation_order[i] == "|":
                    result = int(str(result) + str(d[1][i+1]))
                else:
                    result = result + d[1][i+1]

            if result == d[0]:
                possible = True
                solution = solution + d[0]

print("Solution:", solution)
