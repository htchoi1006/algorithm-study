from collections import deque

n = int(input())
painting = [list(input()) for _ in range(n)]
queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans1, ans2 = 0, 0


def bfs(x, y):
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < n and 0 <= ny < n and painting[nx][ny] == painting[x][y] and not visited[nx][ny]):
                visited[nx][ny] = 1
                queue.append([nx, ny])


visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(not visited[i][j]):
            bfs(i, j)
            ans1 += 1
            
            
for i in range(n):
    for j in range(n):
        if(painting[i][j] == 'G'):
            painting[i][j] = 'R'
            
            
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if(not visited[i][j]):
            bfs(i, j)
            ans2 += 1
            
            
print(ans1, ans2)