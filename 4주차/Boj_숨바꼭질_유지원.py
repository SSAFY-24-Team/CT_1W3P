# 1697. 숨바꼭질
from collections import deque

n, k = map(int, input().split())
max_range = max(n, k) * 2   # 범위설정
visited = [False] * (max_range + 1)


def bfs(x):
    queue = deque([])
    queue.append((x, 0))
    visited[x] = True   # 방문 처리

    while queue:
        x, l = queue.popleft()
        if x == k:
            return l
        else:
            for next in [2*x, x+1, x-1]:
                if 0 <= next <= max_range and not visited[next]:
                    visited[next] = True
                    queue.append((next, l+1))


print(bfs(n))





