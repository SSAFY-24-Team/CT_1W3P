import heapq

n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
sum_v = 0
round = 0

q = []

for i in enemy:
    heapq.heappush(q,-i)
    sum_v += i
    if sum_v > n:
        if k == 0:
            break
        a = -heapq.heappop(q)
        sum_v -= a
        k -= 1

    round += 1


print(round)




