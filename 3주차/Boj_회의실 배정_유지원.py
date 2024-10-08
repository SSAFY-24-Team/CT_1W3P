# 1931. 회의실 배정

n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
et = 0

for s, e in meetings:
    if s >= et:
        et = e
        cnt += 1

print(cnt)