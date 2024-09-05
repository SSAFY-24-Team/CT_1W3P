import copy

di = [0, 0, 0, -1, 1]
dj = [0, -1, 1, 0, 0]

n = int(input())

def click(i, j, board):
    for k in range(5):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 3 and 0 <= nj < 3:
            if board[ni][nj] == '.':
                board[ni][nj] = '*'
            else:
                board[ni][nj] = '.'

def check(board):
    min_count = float('inf')
    check_board = [['.' for _ in range(3)] for _ in range(3)]  

    for array in range(1 << 9):
        copy_board = copy.deepcopy(check_board)
        count = 0

        for i in range(9):
            if array & (1 << i):
                click(i // 3, i % 3, copy_board)
                count += 1

        if copy_board == board:
            min_count = min(min_count, count)

    return min_count

for _ in range(n):
    board = [list(input().strip()) for _ in range(3)]
    answer = check(board)
    print(answer)
