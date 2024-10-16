# 프로그래머스_게임 맵 최단거리
from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    queue = deque([])
    queue.append((0, 0))
    maps[0][0] = 2
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                if nx == n - 1 and ny == m - 1:
                    return maps[nx][ny] - 1
    return -1