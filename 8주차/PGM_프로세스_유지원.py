# 프로그래머스_프로세스

from collections import deque

def solution(priorities, location):
    ans = 0
    queue = deque(priorities)
    while queue:
        process = queue.popleft()
        if queue:
            max_q = max(queue)
        else:
            max_q = 0
        if process < max_q:
            queue.append(process)
            if location == 0:
                location = len(queue) - 1
            else:
                location -= 1
        else:
            ans += 1
            if location == 0:
                return ans
            else:
                location -= 1



# 다른 풀이
from collections import deque


def solution(priorities, location):
    ans = 0
    queue = deque([(i, p) for i, p in enumerate(priorities)])  # (인덱스, 우선순위) 튜플로 저장

    while queue:
        current = queue.popleft()

        # 남아있는 프로세스 중에서 더 높은 우선순위가 있는지 확인
        if any(current[1] < q[1] for q in queue):
            queue.append(current)  # 우선순위가 더 높은 프로세스가 있으면 다시 큐에 넣음
        else:
            ans += 1  # 프로세스를 실행
            if current[0] == location:  # 찾고자 하는 프로세스라면
                return ans  # 현재까지 몇 번째로 실행되었는지 반환
