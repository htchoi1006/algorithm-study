n = int(input())
cmd = input()

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
V = [['#' for j in range(101)] for i in range(101)]

x, y, d = 50, 50, 2
ex = ey = sy = sx = 50
V[x][y] = '.'

for i in cmd:
    if(i == 'L'):
        d = (d+3) % 4
    elif(i == 'R'):
        d = (d+1) % 4
    else:
        x = x + dx[d]
        y = y + dy[d]
        V[x][y] = '.'
        sy, ey, sx, ex = min(sy, y), max(ey, y), min(sx, x), max(ex, x)
        
for i in range(sx, ex+1):
    print(''.join(V[i][sy:ey+1]))