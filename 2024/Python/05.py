data = open('05.txt', 'r').read().split("\n")

rules = []

split = data.index("")

for i in range(split):
    rules.append(data[i].split("|"))

middle_sum = 0
correct_middle_sum = 0
for i in range(split + 1, len(data)):
    u = data[i].split(",")
    uc = []
    uc.extend(u)

    while True:
        changed = False

        for r in rules:
            if u.__contains__(r[0]) and u.__contains__(r[1]) and not u.index(r[0]) < u.index(r[1]):
                uc.remove(r[0])
                uc.insert(u.index(r[1]), r[0])
                changed = True

        if not changed:
            break

    if u == uc:
        middle_sum += int(u[len(u) // 2])
    else:
        correct_middle_sum += int(uc[len(uc) // 2])

print(middle_sum)
print(correct_middle_sum)
