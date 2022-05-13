n,m = map(int, input().split())
board = []

for i in range(n):
    board.append(input())

a, b = 0,0     #a:행, b:열

for i in range(n):
    if("X" not in board[i]):
        a += 1

for j in range(m):
    if("X" not in [board[i][j] for i in range(n)]):
        b += 1

print(max(a,b))