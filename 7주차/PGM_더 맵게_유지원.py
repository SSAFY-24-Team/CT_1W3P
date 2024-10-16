import heapq as hq


# 최솟값을 빨리 뽑을 수 있도록 heap
def solution(scoville, K):
    cnt = 0
    hq.heapify(scoville)  # heap 구조로 바꿔주기

    while len(scoville) > 0:  # 배열 안에 자료가 있을 경우에만
        min_s = hq.heappop(scoville)
        if min_s >= K:
            return cnt
        else:
            if len(scoville) > 0:
                second_s = hq.heappop(scoville)
                new_s = min_s + second_s * 2
                hq.heappush(scoville, new_s)
                cnt += 1
    return -1
