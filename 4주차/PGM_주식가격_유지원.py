# 프로그래머스. 주식가격


def solution(prices):
    n = len(prices)
    ans = [0] * n  # 몇초간

    # prices의 첫번째 부터
    for i in range(n):
        # prices의 그 다음 원소들을 다 비교
        for j in range( i +1, n):
            if prices[i] <= prices[j]:
                ans[i] += 1
            else:  # 작은게 있으면 초 구하고 끝
                ans[i] = j - i
                break
    return ans
