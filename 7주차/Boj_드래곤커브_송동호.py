di = [1,0,-1,0]
dj = [0,-1,0,1]
N = int(input())

arr = [[0]*101 for _ in range(101)]

count = 0

for _ in range(N):
    x,y,d,g = map(int,input().split())

    arr[x][y] = 1

    direction = [d]

    for _ in range(g):
        list1 = direction[::-1]
        for i in list1:
            direction.append((i+1)%4)

    for k in direction:
        ni = x + di[k]
        nj = y + dj[k]
        arr[ni][nj] = 1
        x = ni
        y = nj


for i in range(100):
    for j in range(100):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
            count +=1

print(count)




