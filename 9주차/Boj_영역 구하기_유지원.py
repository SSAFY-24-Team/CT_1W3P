# 2583. 영역 구하기
from collections import deque

# 1. 꼭짓점 -> 칸 변환
# 2. 네모 박스 그리기
# 3. 남은 곳 bfs 하기


def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    paper[x][y] = 1
    s = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and paper[nx][ny] == 0:
                s += 1
                paper[nx][ny] = 1
                queue.append((nx, ny))
    ans.append(s)


m, n, k = map(int, input().split())
paper = [[0] * n for _ in range(m)]
ans = []
for _ in range(k):
    olx, oly, orx, ory = map(int, input().split())
    lx = m - 1 - oly
    ly = olx
    rx = m - ory
    ry = orx - 1
    # print(lx, ly, rx, ry)
    # 2. 직사각형 그리기
    row = 0
    nrx = rx
    while row < (lx - rx + 1):
        for i in range(ry-ly+1):
            paper[nrx][ly + i] = 1   # 직사각형의 왼쪽위 칸
        row += 1
        nrx += 1
# for i in range(m):
#     print(*paper[i])
# 빈 칸 bfs
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0:
            bfs(i, j)

print(len(ans))
ans.sort()
print(*ans)
