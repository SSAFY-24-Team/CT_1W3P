# 프로그래머스_최솟값 만들기
# pop() - O(1)
# pop(n) - O(N)
# remove(n) - O(N)

def solution(A, B):
    ans = 0
    A.sort()
    B.sort()

    while A:
        min_a = A[0]
        min_b = B[0]
        max_a = A[-1]
        max_b = B[-1]

        if min_a < min_b:
            ans += min_a * max_b
            A.pop(0)
            B.pop()
        else:
            ans += min_b * max_a
            A.pop()
            B.pop(0)

    return ans