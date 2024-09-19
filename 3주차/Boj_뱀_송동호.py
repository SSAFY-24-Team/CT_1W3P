di = [0,0,1,-1]
dj = [1,-1,0,0]

N = int(input())
K = int(input())

i,j =0,0
d = 0
snake_l = 1
snake = [(0,0)]

arr = [[0]*N for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1

L = int(input())

directions = []

cnt= 0

for _ in range(L):

    c,e = input().split()
    c = int(c)

    while True:

        if cnt == c:
            if d == 0 and e == "L":
                d = 3
            elif d == 0 and e == "R":
                d = 2
            elif d == 1 and e == "L":
                d = 2
            elif d == 1 and e == "R":
                d = 3
            elif d == 2 and e == "L":
                d = 0
            elif d == 2 and e == "R":
                d = 1
            elif d == 3 and e == "L":
                d = 1
            elif d == 3 and e == "R":
                d = 0
            break
        for i in snake:

            i = i + di[d]
            j = j + dj[d]
            cnt += 1









