# 8-7. 가장 높은 탑 쌓기

n = int(input())
info = []
dy = [0] * n  # info[i]가 마지막 벽돌(제일 밑에 벽돌)일 때, 최대 높이
for i in range(n):
    s, h, w = map(int, input().split())
    info.append((s, h, w, i+1))
# 면적 오름차순 정렬 (기준 하나 고정)
info.sort()

# LIS 찾기 (무게 기준으로 최대 증가 부분수열 길이 구하기)
dy[0] = info[0][1]
dyy = [[] for _ in range(n)]
dyy[0] = [info[0][3]]
tmp = 0   # 비교용
for i in range(1, n):
    tmp = 0
    tmp_info = []
    for j in range(i):
        if info[i][2] > info[j][2]:
            # dy[i] = max(dy[j] + info[i][1], dy[i])
            if tmp < dy[j] + info[i][1]:
                tmp = dy[j] + info[i][1]
                tmp_info = dyy[j][:]
    dy[i] = tmp
    dyy[i] = tmp_info
    dyy[i].append(info[i][3])
    if dy[i] == 0:   # 제일 작을 경우도 고려
        dy[i] = info[i][1]
        dyy[i] = [info[i][3]]

idx = dy.index(max(dy))
print(len(dyy[idx]))
for i in dyy[idx]:
    print(i)