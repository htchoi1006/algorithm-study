from collections import deque

field = [list(input()) for _ in range(12)]
# field = [['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.'], ['.', 'Y', '.', '.', '.', '.'], ['.', 'Y', 'G', '.', '.', '.'], ['R', 'R', 'Y', 'G', '.', '.'], ['R', 'R', 'Y', 'G', 'G', '.']]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    tmp.append((x, y))
    
    while queue:
        a, b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == field[x][y] and visited[nx][ny] == 0:
                queue.append((nx, ny))
                tmp.append((nx, ny))
                visited[nx][ny] = 1
    
    
    
def delete(tmp):
    for x, y in tmp:
        field[x][y] = '.'
        

        
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if field[j][i] != '.' and field[k][i] == '.':
                    field[k][i] = field[j][i] 
                    field[j][i] = '.'
                    break
    
    
ans = 0

while 1:
    flag = 0
    visited = [[0]*6 for _ in range(12)]
    
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                tmp = []
                bfs(i, j)

                if len(tmp) >= 4:
                    flag = 1
                    delete(tmp)


    if flag == 0:
        break

    down()
    ans += 1
                
                
                
print(ans)
                
                
                
