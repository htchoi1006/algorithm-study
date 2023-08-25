from collections import deque

n, m = map(int, input().split())
campus = []
start = ()

for i in range(n):
    row = list(input())
    for j in range(m):
        if(row[j] == 'I'):
            start = (i, j)
    campus.append(row)

    
direction = [(1,0), (0,1), (-1,0), (0, -1)]
visited = [[False]*m for _ in range(n)]
num_people = 0 #만날 수 있는 사람의 수

queue = deque([start])

visited[start[0]][start[1]] = True

while(queue):
    x, y = queue.popleft()

    
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        
        if(0 <= nx < n) and (0 <= ny < m):
            if(campus[nx][ny] != 'X') and not (visited[nx][ny]):
                queue.append((nx, ny))
                visited[nx][ny] = True
                
                if(campus[nx][ny] == 'P'):
                    num_people += 1
                    
                    
print(num_people if num_people > 0 else 'TT')