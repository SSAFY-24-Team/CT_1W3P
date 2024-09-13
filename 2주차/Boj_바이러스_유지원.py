from collections import deque


def bfs(graph, node, visited):
    global cnt
    # bfs 선입선출 deque 사용
    queue = deque([node])
    # 방문처리
    visited[node] = True

    # queue가 빌 때까지
    while queue:
        v = queue.popleft()  # 꺼내고
        cnt += 1  # 갑니다
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True  # 방문처리
                queue.append(i)


n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
cnt = -1

for _ in range(m):
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)

for i in range(1, n+1):
    g[i].sort()

visited = [False] * (n+1)
bfs(g, 1, visited)
print(cnt)