from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, a, b = map(int, input().split())
virus = []

# n, k = 3, 3
# arr = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
# s, a, b = 2, 3, 2


for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus.append((arr[i][j], i, j))
            
virus.sort(key = lambda x: x[0])

queue = deque(virus)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

while queue:
    if count == s:
        break
    for _ in range(len(queue)):
        state, x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = state
                queue.append((arr[nx][ny], nx, ny))
            
    count += 1
    
print(arr[a-1][b-1])
    
    
    
    
    
    
    
    
    
    