N = int(input())

arr = [[0]*N for _ in range(N)]

lsts = [list(map(int,input().split())) for _ in range(N**2)]

for lst in lsts:
    mx,empty_max = -1,-1

    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                continue


