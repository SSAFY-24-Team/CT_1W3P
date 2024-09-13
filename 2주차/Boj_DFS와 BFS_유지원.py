# DFS와 BFS
from collections import deque


def dfs(graph, node, visited):
    # 맨 처음 시작 노드 방문 처리
    visited[node] = True
    # 방문한 경로 출력
    print(node, end=' ')
    # 인접 노드 탐색
    for i in graph[node]:
        # 방문하지않았다면
        if not visited[i]:
            # 방문 처리
            visited[i] = True
            # 재귀
            dfs(graph, i, visited)


def bfs(graph, node, visited):
    # bfs는 queue로 선입선출이용
    queue = deque([node])
    # 방문 처리
    visited[node] = True

    # queue를 다 비울때까지
    while queue:
        v = queue.popleft()
        # 방문 경로 출력
        print(v, end=' ')
        # 인접 노드 탐색
        for i in graph[v]:
            if not visited[i]:
                # 큐에 더해줌(대기)
                queue.append(i)
                # 방문 처리
                visited[i] = True


n, m, v = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)
# 낮은 숫자부터 방문하기위한 sort o(nlogn)
for i in range(1, n+1):
    g[i].sort()

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)
dfs(g, v, visited1)
print()
bfs(g, v, visited2)