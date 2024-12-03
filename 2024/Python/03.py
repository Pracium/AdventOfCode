import re
pattern = re.compile("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)")

sum = 0
sum_enabled = 0
enabled = True
for m in pattern.findall(open('03.txt', 'r').read()):
    if m == "do()":
        enabled = True
    elif m == "don't()":
        enabled = False
    else:
        m = m.replace("mul(", "").replace(")", "").split(",")
        prod = int(m[0]) * int(m[1])
        sum += prod
        if enabled:
            sum_enabled += prod

print("Sum of all multiplications: ", sum)
print("Sum of all enabled multiplications: ", sum_enabled)
