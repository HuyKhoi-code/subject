def isSafe (x, y, board, n, m):
    if (x>=0 and y>=0 and x<n and y<m and board[x][y]==1):
        return True
    return False
def Result (board, n, m):
    for i in range(n):
        for j in range(m):
            print (board[i][j], end=" ")
        print ()
def KnightRoute(n, m, cur_x, cur_y):
    board = [[-1]*n for _ in range(m)]
    next_x = [2, 1, -1, -2, -2, -1, 1, 2]
    next_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[cur_x][cur_y] = 0
    pos = 1
    if (not Solution(board, n, m, cur_x, cur_y, next_x, next_y, pos)):
        print ('khong tim thay')
    else:
        Result(board, n, m)
def Solution(board, n, m, cur_x, cur_y, next_x, next_y, pos):
    if pos == n*m:
        return True
    for i in range(8):
        new_x = cur_x + next_x
        new_y = cur_y + next_y
        if (isSafe(new_x, new_y, board, n, m)):
            board[new_x][new_y] == pos
            if (Solution(board, n, m, cur_x, cur_y, next_x, next_y, pos+1)):
                return True
            board[new_x][new_y = -1]
    return False

n, m = list(map(int, input().split()))

vitri = input()
y = vitri[0]
x = vitri[1]
print (x, y)

y = ord(y) - 97
x = int(x)-1

KnightRoute(n, m, x, y)

