# 촌수계산
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 0
    while q:
        node = q.popleft()
        for nxt in adj[node]:
            if visit[nxt] == -1:
                visit[nxt] = visit[node]+1
                q.append(nxt)


n = int(input())
a, b = map(int, input().split(' '))
m = int(input())
adj = [[] for _ in range(n+1)]
visit = [-1] * (n+1)
for i in range(m):
    x, y = map(int, input().split(' '))
    adj[x].append(y)
    adj[y].append(x)
bfs(a)

print(visit[b])