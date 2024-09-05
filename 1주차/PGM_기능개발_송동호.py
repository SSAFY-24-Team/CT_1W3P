from collections import deque

progresses = [50, 50, 50]
speeds = [1, 99, 1]

q= deque()
answer = []

for i in range(3):
    a = progresses[i]
    b = speeds[i]
    c = (100-a)//b
    d = (100-a)%b

    if d == 0:
        q.append(c)
    else:
        q.append(c+1)

a2 = q[0]
num = 1

for i in range(1, len(q)):
    if q[i] <= a2:
        num += 1
    else:
        answer.append(num)
        a2 = q[i]
        num = 1

answer.append(num)


print(answer)




