a = list(map(int,input()))


num1 = 0
num2 = 0

while True:
    list1 = []
    for i in a:
        if i == 0:
            num1 += 1
        elif i == 1:
            list1.append(i)

    list2 = []
    num = len(list1)
    while True:
        list2.append(num % 2)
        num = num//2

        if num == 0:
            num2 += 1
            break

    if len(list2) == 1:
        break

    a = list2

print(num1)
print(num2)