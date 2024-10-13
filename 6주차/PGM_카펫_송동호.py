brown  = 24
yellow = 24

list1 = []
answer1 = 0
answer2 = 0


for i in range(1,int(yellow**0.5) + 1):
    if yellow%i == 0:
        list1.append(i)

list1.sort()

for i in range(len(list1)):
    sum_v = 0
    a = list1[i]
    b = yellow//a

    sum_v += (b+2)*2
    sum_v += 2*a

    if sum_v == brown:
        answer1 = b+2
        answer2 = a+2
        break

print(answer1,answer2)





