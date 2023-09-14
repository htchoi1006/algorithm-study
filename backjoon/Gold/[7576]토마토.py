from collections import deque

m, n = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
queue = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
res = 0

for i in range(n):
    for j in range(m):
        if(arr[i][j] == 1):
            queue.append([i, j])
            
            
def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if(0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0):
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])
                
bfs()

for i in arr:
    for j in i:
        if(j == 0):
            print(-1)
            exit(0)
            
    res = max(res, max(i))
print(res - 1)