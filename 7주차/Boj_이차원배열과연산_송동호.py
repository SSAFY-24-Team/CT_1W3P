r,c,k = map(int,input().split())


arr = [list(map(int, input().split())) for _ in range(3)]

r -= 1
c -= 1

for ans in range(101):
    if 0<= r < len(arr) and 0<= c < len(arr[0]) and arr[r][c] == k:
        break

    rmode = 1

    if len(arr) < len(arr[0]):
        rmode = 0
        arr = list(map(list,zip(*arr)))
    mxcol = 0


    for i in range(len(arr)):
        cnt = {}
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                continue
            if arr[i][j] in cnt:
                cnt[arr[i][j]] += 1
            else:
                cnt[arr[i][j]] = 1

        list1 = sorted(cnt.items(),key=lambda x:(x[1],x[0]))

        new = []

        for lst in list1:
            for n in lst:

                new.append(n)

        arr[i] = new

        mxcol = max(mxcol, len(arr[i]))

    mxcol = min(mxcol, 100)

    for i in range(len(arr)):
        while len(arr[i]) < mxcol:
            arr[i].append(0)

        while len(arr[i]) > mxcol:
            arr[i].pop()



    if rmode == 0:
        arr = list(map(list, zip(*arr)))


else:
    ans = -1

print(ans)
