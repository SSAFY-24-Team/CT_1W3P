# 프로그래머스_올바른 괄호
def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                answer = False
                return answer
    if not stack:
        return answer
    else:
        answer = False
        return answer
    