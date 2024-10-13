a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()

sum_v = 0

for i in range(len(a)):
    a1 = a[i]
    b1 = b.pop()

    sum_v += a1*b1

print(sum_v)

