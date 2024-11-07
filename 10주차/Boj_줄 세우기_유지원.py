# 2252. 줄 세우기 (위상 정렬)
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
# graph = [[0] * (n+1) for _ in range(n+1)] 메모리초과
# 이 그래프는 n^2 * 4byte(정수) 대략 3.81GB 메모리
# degree[i]: i 학생이 앞에 몇 명의 학생이 있어야하는지
degree = [0] * (n+1)   # 진입차수
queue = deque([])
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    print(student, end=" ")
    for i in graph[student]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)
