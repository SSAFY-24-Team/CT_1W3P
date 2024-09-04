# 백준 15650 N과 M(2)

n, m = map(int, input().split())
res = [0] * m


def dfs(l, s):   # s : 시작 숫자
    if l == m:
        print(*res)
        return
    else:
        for i in range(s, n+1):
            res[l] = i
            dfs(l+1, i+1)   # 그 다음 수부터 사용할 수 있도록


dfs(0, 1)