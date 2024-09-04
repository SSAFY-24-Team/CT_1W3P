# 백준 15649 N과 M(1)

n, m = map(int, input().split())
ch = [0] * (n+1)  # 중복 제거 용도, 체크 했는지 여부
res = [0] * m


# 트리만들기
def dfs(l):
    if l == m:  # m개 다 뽑았을 때 끝
        print(*res)
        return
    else:
        for i in range(1, n+1):
            if ch[i] == 0:  # 쓰지않은 숫자라면
                res[l] = i  # 그 숫자 사용
                ch[i] = 1  # 사용했다고 체크
                dfs(l+1)
                ch[i] = 0  # 초기화(i는 계속 증가하므로 이전것에 영향x)


dfs(0)