k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
count = 0

gul = [0]*6

for i in tangerine:
    gul[i] += 1

print(max(gul))
print(gul)


while True:
    if k <= 0:
        break
    a = gul.index(max(gul))
    count += 1
    k -= max(gul)
    gul[a] = 0

print(count)