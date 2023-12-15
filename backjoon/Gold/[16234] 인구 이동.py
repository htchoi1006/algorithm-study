from collections import deque

n, l, r = map(int, input().split())
# n, l, r = 2, 20, 50
world = [list(map(int, input().split())) for _ in range(n)]
# world = [[50, 30], [20, 40]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    queue = deque()
    tmp = []
    
    queue.append((a, b))
    tmp.append((a, b))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            xy = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(world[nx][ny] - world[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    tmp.append((nx, ny))
                    
    return tmp



    
result = 0

while 1:
    visited = [[0] * (n+1) for _ in range(n+1)]
    flag = 0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)
                
                if len(country) > 1:
                    flag = 1
                    number = sum([world[x][y] for x, y in country]) // len(country)
                    
                    for x, y in country:
                        world[x][y] = number
                        
                        
    if flag == 0:
        break
    result += 1
    
print(result)