n,s = map(int,input().split())

num1 = list(map(int,input().split()))

result = 10000000

for i in range(n):

    left,right =i,i

    count = 0

    while right < len(num1) :
        sum1 = sum(num1[left:right])
        if sum1 >= s:
            result = min(count,result)
            break
        else:
            count += 1
            right += 1

print(result)


