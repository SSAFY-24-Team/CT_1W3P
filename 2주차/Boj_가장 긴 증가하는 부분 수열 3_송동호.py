def igin(target):

    left,right = 0, len(dp)-1
    best = 0
    while left <= right:
        mid = (left+right)//2

        if dp[mid] < target:
            left = mid + 1

        else:
            best = mid
            right = mid -1
    return best

n = int(input())

num = list(map(int,input().split()))

dp = []

dp.append(num[0])

for i in range(1,n):
    if num[i] > dp[-1]:
        dp.append(num[i])
    else:
        best = igin(num[i])
        dp[best] = num[i]

print(len(dp))


