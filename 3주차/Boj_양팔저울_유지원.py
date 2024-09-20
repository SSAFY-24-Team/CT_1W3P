# 17610. 양팔저울
import sys


def dfs(l, s):
    # 가지치기 (남은 모든걸 더해도 0이하면 그만 계산하기)
    if s + sum(weight[l:]) <= 0:
        return
    # 마지막까지 돌았을 때
    if l == k:
        # 양수라면
        if 0 < s:
            # res라는 set에 더하기
            # 처음에는 list에서 not in -> remove로 했는데 시간 초과
            res.add(s)
    else:
        # 상태트리 그리기
        # 나 다음 순서부터 추를 더하거나, 반대쪽에 넣거나, 추를 넣지않는 경우 나누기
            dfs(l+1, s + weight[l])  # 추를 더한 경우
            dfs(l+1, s - weight[l])  # 추를 반대편에 놓은 경우(뺀 경우)
            dfs(l+1, s)  # 추를 놓지않은 경우


k = int(input())
weight = list(map(int, sys.stdin.readline().rstrip().split()))
res = set()  # 중복방지, 시간 더 빠름

# 여러가지 경우의 수를 고려해야하는 경우 0부터 시작
dfs(0, 0)  # 0부터 시작!!!

print(sum(weight) - len(res))