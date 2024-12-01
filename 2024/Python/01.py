data = open('01.txt', 'r').read().split('\n')

left = []
right = []

for d in data:
    left.append(int(d.split("   ")[0]))
    right.append(int(d.split("   ")[1]))

left.sort()
right.sort()

total_distance = 0

for i in range(len(data)):
    total_distance += abs(left[i] - right[i])

similarity_score = 0

for l in left:
    count = 0

    for r in right:
        if r == l:
            count += 1

    similarity_score += l * count

print("Total distance:", total_distance)
print("Similarity score:", similarity_score)
