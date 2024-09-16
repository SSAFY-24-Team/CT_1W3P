# 2178. 미로탐색
import sys
from collections import deque


def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                if g[x+dx[i]][y+dy[i]] == 1:
                    queue.append((x+dx[i], y+dy[i]))
                    g[x+dx[i]][y+dy[i]] = g[x][y] + 1


n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().rstrip())))
bfs(0, 0)


print(g[n-1][m-1])