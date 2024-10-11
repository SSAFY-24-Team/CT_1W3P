# 10799. 쇠막대기

info = list(input())
stack = []
present = 0
ans = 0

for i in info:
    if not stack:
        stack.append(i)
    else:
        if stack[-1] == '(' and i == '(':
            present += 1
            ans += 1
        elif stack[-1] == '(' and i == ')':
            ans += present
        elif stack[-1] == ')' and i == ')':
            present -= 1
        stack.append(i)

print(ans)