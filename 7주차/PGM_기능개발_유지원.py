# 프로그래머스_기능개발

def solution(progresses, speeds):
    days = []
    ans = []
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i] != 0:
            days.append((100 - progresses[i])//speeds[i] + 1)
        else:
            days.append((100 - progresses[i])//speeds[i])
    # 걸리는 시간 배열 완성
    stack = [days[0]]   # stack에 넣고 크기 비교
    i = 1
    print(stack)
    while i < len(days):
        if stack[0] >= days[i]:
            stack.append(days[i])
        else:
            ans.append(len(stack))
            stack = [days[i]]
        i += 1
    ans.append(len(stack))
    return ans