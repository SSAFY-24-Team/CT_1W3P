# 백준 15686 치킨 배달
# 재귀 호출에서 독립적인 리스트가 필요하다면,
# 매번 새로운 리스트를 만들어야 하고, 그렇지 않으면 이전 호출에서 사용한 리스트가 그대로 다음 호출에 영향을 미칩니다.
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
pizza = []


res = 2147000000


def dfs(l, x, tmp):
    global res
    if l == m:   # 조합 (피자집들 중에서 m개의 피자집만 뽑는)
        if res > sum(tmp):
            res = sum(tmp)
            return
    else:
        for j in range(x, len(pizza)):  # 조합
            tmp_n = [0] * len(house)   # 거리비교 new 버전
            for i in range(len(house)):  # 거리 비교
                new = abs(pizza[j][0] - house[i][0]) + abs(pizza[j][1] - house[i][1])
                # print(f'j : {j}, i : {i}, tmp: {tmp}, n: {n} new: {new}')
                if tmp[i] > new:  # 더 가까운 피자 가게가 있다면
                    tmp_n[i] = new  # 거리 다시 설정
                else:
                    tmp_n[i] = tmp[i]  # 아니라면 그대로
            dfs(l+1, j+1, tmp_n)  # 그 다음 조합만들기


# 1. 집, 피자 찾기
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            pizza.append((i, j))

t = [2347000000] * len(house)


# 2. 거리 계산
dfs(0, 0, t)
print(res)

# ------------------------------------
# 더 간단한 방법 (단계별로 나눠서 풀기)
n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
house = []
pizza = []
com = []
tot = 2147000000

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            house.append((i, j))
        elif map[i][j] == 2:
            pizza.append((i, j))


# 2. 조합 구하기

def dfs(l, x):
    global tot
    if l == m:
        # 피자배달거리
        # 한 집에 가장 가까운 피자집
        res = 0
        for i in range(len(house)):
            x1, y1 = house[i][0], house[i][1]
            dis = 2147000000
            for j in com:
                x2, y2 = pizza[j][0], pizza[j][1]
                dis = min(dis, (abs(x1 - x2) + abs(y1 - y2)))
            res += dis   # 각 집들의 피자 배달 거리를 합한 것
        tot = min(tot, res)  # 조합들 중에서 최소 총 거리
        return
    else:
        for i in range(x, len(pizza)):
            com.append(i)
            dfs(l+1, i+1)
            com.pop()


dfs(0, 0)
print(tot)