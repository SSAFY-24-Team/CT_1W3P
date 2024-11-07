# 2252. 줄 세우기 (위상 정렬)
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
ans = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    degree[b] += 1

# 진입차수가 0인 것 중에 가장 쉬운 것(가장 번호가 낮은 것)
# 항상 가장 작은 값을 반복적으로 꺼내야하므로 빠르게 할 수 있는 "우선순위 큐" 사용
heap = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(heap, i)     # heap에 i를 push

# 위상정렬
while heap:
    p = heapq.heappop(heap)
    print(p, end=" ")
    for nxt_p in graph[p]:
        degree[nxt_p] -= 1
        if degree[nxt_p] == 0:
            heapq.heappush(heap, nxt_p)



