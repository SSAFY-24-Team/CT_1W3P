# 백준 15651 N과 M(3)

n, m = map(int, input().split())
res = [0] * m


def dfs(l):
    if l == m:
        print(*res)
        return
    else:
        for i in range(1, n+1):  # 중복허용
            res[l] = i
            dfs(l+1)


dfs(0)