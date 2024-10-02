# 7-15. 토마토(BFS 활용)
import sys
from collections import deque


def bfs(init):
    global days
    queue = deque([])
    for x, y in init:
        queue.append((x, y, days))

    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = 1  # 토마토 익힘
                    queue.append((nx, ny, d+1))
                    days = d+1
                    # print(f'bfs내부 : {days}')


m, n = map(int, input().split())
tomatos = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
all = True   # 모든 토마토가 익었을 때
init_list = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
days = 0
not_all = False  # 안익은 토마토가 있을 때

# 저장될 때부터 모든 토마토가 익어있는 상태
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            init_list.append((i, j))
        else:
            all = False   # 0을 만나면 모든 토마토가 익은게 아님
if all:
    print(0)
else:
    bfs(init_list)

# 익지 못하는 상황인지 확인
for i in range(n):
    if not_all:
        break
    for j in range(m):
        if tomatos[i][j] == 0:
            print(-1)
            not_all = True
            break

if not not_all and not all:
    print(days)


# 2번째 방법 (더 간단)
# 7-15. 토마토(BFS 활용)
import sys
from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tomatos[nx][ny] == 0:
                    tomatos[nx][ny] = 1  # 토마토 익힘
                    queue.append((nx, ny))
                    days[nx][ny] = days[x][y] + 1

    ans = 0

    for i in range(n):
        if 0 in tomatos[i]:   # 토마토가 모두 익지는 못하는 상황
            print(-1)
            return
        ans = max(max(days[i]), ans)    # 최댓값 찾기
    print(ans)
    return


m, n = map(int, input().split())
tomatos = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
queue = deque([])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
days = [[0] * m for _ in range(n)]  # 날짜 체크

for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            queue.append((i, j))

bfs()


