# 1012. 유기농 배추
from collections import deque

t = int(input())


def bfs(x, y):
    queue = deque([[x, y]])
    batu[x][y] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and batu[nx][ny] == 1:
                batu[nx][ny] = 0
                queue.append([nx, ny])


for _ in range(t):
    m, n, k = map(int, input().split())
    batu = [[0] * n for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        batu[x][y] = 1

    for i in range(m):
        for j in range(n):
            if batu[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)



