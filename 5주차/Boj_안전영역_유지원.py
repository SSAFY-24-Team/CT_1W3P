# 7-14. 안전영역(BFS)
import sys
from collections import deque


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and map[nx][ny] > high:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


n = int(input())
map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
high_set = set()
visited = [[0] * n for _ in range(n)]
cnt = 0
max_cnt = -2147000000

for i in range(n):
    for j in range(n):
        high_set.add(map[i][j])
# print(high_set)

for high in high_set:
    for i in range(n):
        for j in range(n):
            if map[i][j] > high:
                if visited[i][j] == 0:
                    cnt += 1
                    bfs(i, j)
    if cnt >= max_cnt:
        # print(f'high: {high}, max_cnt: {max_cnt}, cnt: {cnt}')
        max_cnt = cnt
        cnt = 0
        visited = [[0] * n for _ in range(n)]
    else:
        # print(f'high: {high}, max_cnt: {max_cnt}, cnt: {cnt}')
        cnt = 0
        visited = [[0] * n for _ in range(n)]
    #     break

if max_cnt == 0:
    print(max_cnt+1)
else: print(max_cnt)
