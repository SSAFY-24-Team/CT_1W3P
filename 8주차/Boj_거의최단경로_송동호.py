import heapq



def dix(start, end):
    q = []
    node = [None] * N
    distance = [float('inf')] * N
    v = [0] * N
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        current_dis, current_node = heapq.heappop(q)

        if v[current_node]:
            continue

        v[current_node] = 1

        for next_node in range(N):
            if arr[current_node][next_node] != 0 and v[next_node] == 0:
                new_dis = arr[current_node][next_node] + current_dis
                if new_dis < distance[next_node]:
                    distance[next_node] = new_dis
                    node[next_node] = current_node
                    heapq.heappush(q, (new_dis, next_node))
    return node, distance[end]


def chase(node, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = node[current_node]
    path.append(start)

    path.reverse()

    return path


while True:

    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    S, D = map(int, input().split())

    arr = [[0] * N for _ in range(N)]

    result = 0

    for _ in range(M):
        U, V, P = map(int, input().split())
        arr[U][V] = P

    node, dis = dix(S, D)
    if dis == float('inf'):
        print(-1)
        continue

    while True:
        path = chase(node, S, D)
        for i in range(len(path) - 1):
            arr[path[i]][path[i + 1]] = float('inf')

        node, new_dis = dix(S, D)
        if new_dis != dis:
            result = new_dis
            break

    if result == float('inf'):
        print(-1)
    else:
        print(result)