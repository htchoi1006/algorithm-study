c, r = map(int, input().split())
seat = int(input())

# c, r = 7, 6
# seat = 11

if seat > c*r:
    print(0)
    exit()

dx = [0, 1, 0, -1] 
dy = [-1, 0, 1, 0]

grid = [[0]*c for _ in range(r)]
direction = x = y = 0

for i in range(1, c*r+1):
    if i == seat:
        print(y+1, x+1)
        break
        
    else:
        grid[x][y] = i
        x += dx[direction]
        y += dy[direction]
        
        if x < 0 or x >= r or y < 0 or y >= c or grid[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            
            direction = (direction + 1)%4
            
            x += dx[direction]
            y += dy[direction]
        