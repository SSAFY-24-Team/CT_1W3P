N,d,k,c = map(int,input().split())

chobap = []

s = [0] * (d+1)
s[c] = 1
count = 1

for _ in range(N):
    num = int(input())
    chobap.append(num)

for i in range(k):
    s[chobap[i]] += 1
    if s[chobap[i]] == 1:
        count += 1

answer = count

for i in range(N):
    s[chobap[i]] -= 1

    if s[chobap[i]] == 0:
        count -= 1
    s[chobap[(i+k)%N]] += 1

    if s[chobap[(i+k)%N]] == 1:
        count += 1
    answer = max(answer,count)


print(answer)




