from collections import deque

s = input()
a = deque()
flag = True

for i in s:
    if i == "(":
        a.append(i)
    else:
        if a:
            a.pop()
        else:
            flag = False
if a:
    flag = False

print(flag)

