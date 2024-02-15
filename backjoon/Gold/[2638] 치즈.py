import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# n, m = 8, 9
# graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
time = 0

#외부 공기를 2로 변환
def background(a, b, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    graph[a][b] = 2
    visited[a][b] = 1
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny] == 2):
                visited[nx][ny] = 1
                graph[nx][ny] = 2
                
                background(nx, ny, visited)
            

#외부 공기와 맣다은 개수 체크
def arround(a, b):
    cnt = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        if graph[nx][ny] == 2:
            cnt += 1
            
    return cnt



while True:
    time += 1
    visited = [[0]*m for _ in range(n)]
    background(0, 0, visited)
    melt = []


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and arround(i, j) > 1:
                melt.append((i, j))


    for x, y in melt:
        graph[x][y] = 2

        
    flag = True
    for i in graph:
        if i.count(1) != 0:
            flag = False
    
    if flag:
        break
    
    
    
print(time)
    
    