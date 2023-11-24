from collections import deque

n = int(input())
game = [[0]*n for _ in range(n)]

k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    game[x-1][y-1] = 2

l = int(input())
queue = deque()
dirDict = dict()
queue.append((0, 0))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



for _ in range(l):
    x, c = input().split()
    dirDict[int(x)] = c
    
x, y = 0, 0
game[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    
    if alpha == 'L':
        direction = (direction - 1)%4
    elif alpha == 'D':
        direction = (direction + 1)%4

while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    
    if game[x][y] == 2:  #사과일때
        game[x][y] == 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])
            
            
    elif game[x][y] == 0:
        game[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        game[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])
            
    else:
        break
        
print(cnt)
    



        