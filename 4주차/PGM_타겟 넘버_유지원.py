# 프로그래머스. 타겟 넘버
cnt = 0  # 전역변수 설정


def solution(numbers, target):
    # 상태트리 dfs 이용(0부터 시작, numbers 순회하며 +,- 두가지 상태로 나눔)
    def dfs(l, tot):
        global cnt
        if l == len(numbers):
            if tot == target:
                cnt += 1
                return
        else:
            dfs(l + 1, tot + numbers[l])
            dfs(l + 1, tot - numbers[l])

    dfs(0, 0)

    answer = 0
    return cnt