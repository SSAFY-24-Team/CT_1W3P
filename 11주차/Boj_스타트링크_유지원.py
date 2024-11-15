# 5014. 스타트링크
from collections import deque

# 방문체크!!!!!!
def bfs():
    queue = deque([])
    queue.append([s, 0])
    visited[s] = 1
    elev = [u, -d]

    while queue:
        floor, cnt = queue.popleft()
        if floor == g:
            print(cnt)
            return
        for i in elev:
            new = floor + i
            if 0 < new <= f and visited[new] == 0:
                visited[new] = 1
                queue.append([new, cnt + 1])

    print(no)


f, s, g, u, d = map(int, input().split())
visited = [0] * (f+1)
no = "use the stairs"
# 못가는 경우
if g < s and d == 0:   # 1. 사무실이 더 낮은데 내려가는 층이 없는 경우
    print(no)
elif g > s and u == 0:   # 2. 사무실이 더 높은데 올라가는 층이 없는 경우
    print(no)
else:
    bfs()







