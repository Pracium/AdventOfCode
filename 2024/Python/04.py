data = open('04.txt', 'r').read().replace("\n", "")
line_length = len(open('04.txt', 'r').read().split('\n'))

xmas_count = data.count("XMAS") + data.count("SAMX")
x_mas_count = 0

for i in range(len(data)):
    if data[i] == 'X':
        if i + line_length * 3 < len(data):
            if data[i + line_length] == 'M' and data[i + line_length * 2] == 'A' and data[i + line_length * 3] == 'S' and abs(i // line_length - (i + line_length * 3) // line_length) == 3:
                xmas_count += 1
        if i - line_length * 3 >= 0:
            if data[i - line_length] == 'M' and data[i - line_length * 2] == 'A' and data[i - line_length * 3] == 'S' and abs(i // line_length - (i - line_length * 3) // line_length) == 3:
                xmas_count += 1
        if i + line_length * 3 + 3 < len(data):
            if data[i + line_length + 1] == 'M' and data[i + line_length * 2 + 2] == 'A' and data[i + line_length * 3 + 3] == 'S' and abs(i // line_length - (i + line_length * 3 + 3) // line_length) == 3:
                xmas_count += 1
        if i + line_length * 3 - 3 < len(data):
            if data[i + line_length - 1] == 'M' and data[i + line_length * 2 - 2] == 'A' and data[i + line_length * 3 - 3] == 'S' and abs(i // line_length - (i + line_length * 3 - 3) // line_length) == 3:
                xmas_count += 1
        if i - line_length * 3 + 3 >= 0:
            if data[i - line_length + 1] == 'M' and data[i - line_length * 2 + 2] == 'A' and data[i - line_length * 3 + 3] == 'S' and abs(i // line_length - (i - line_length * 3 + 3) // line_length) == 3:
                xmas_count += 1
        if i - line_length * 3 - 3 >= 0:
            if data[i - line_length - 1] == 'M' and data[i - line_length * 2 - 2] == 'A' and data[i - line_length * 3 - 3] == 'S' and abs(i // line_length - (i - line_length * 3 - 3) // line_length) == 3:
                xmas_count += 1

for i in range(len(data)):
    if data[i] == 'A':
        try:
            if ((data[i - line_length - 1] == 'M' and data[i - line_length + 1] == 'M' and data[i + line_length - 1] == 'S' and data[i + line_length + 1] == 'S'
                    or data[i - line_length - 1] == 'S' and data[i - line_length + 1] == 'S' and data[i + line_length - 1] == 'M' and data[i + line_length + 1] == 'M'
                    or data[i - line_length - 1] == 'M' and data[i - line_length + 1] == 'S' and data[i + line_length - 1] == 'M' and data[i + line_length + 1] == 'S'
                    or data[i - line_length - 1] == 'S' and data[i - line_length + 1] == 'M' and data[i + line_length - 1] == 'S' and data[i + line_length + 1] == 'M')
                    and abs(i // line_length - (i - line_length - 1) // line_length) == 1 and abs(i // line_length - (i + line_length + 1) // line_length) == 1):
                x_mas_count += 1
        except:
            pass

print(xmas_count)
print(x_mas_count)
