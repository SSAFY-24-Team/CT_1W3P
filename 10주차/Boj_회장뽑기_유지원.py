# 8-13. 회장뽑기(플로이드-워샬 응용)
# 플로이드 와샬 알고리즘: 모든 정점에서 모든 정점까지 최단 경로

# 친구 n을 경유하여 얻을 수 있는 점수의 최소값
n = int(input())
dy = [[500] * (n) for _ in range(n)]
for i in range(n):
    dy[i][i] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        dy[a-1][b-1] = 1
        dy[b-1][a-1] = 1

# 친구 k번 경유
for k in range(n):
    for i in range(n):
        for j in range(n):
            dy[i][j] = min(dy[i][j], dy[i][k]+dy[k][j])


scores = []
for i in range(n):
    scores.append(max(dy[i]))

min_s = min(scores)
cnt = 0
ans = []

for i in range(n):
    if scores[i] == min_s:
        cnt += 1
        ans.append(i+1)

print(min_s, cnt)
print(*ans)










