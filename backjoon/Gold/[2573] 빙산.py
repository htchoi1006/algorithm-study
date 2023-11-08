from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    sea = []
    
    while queue:
        x, y = queue.popleft()
#         print(x, y)
        
        num_sea = 0
        
        for i in range(4):   #주변 바다개수 카운트
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:  #바다면
                    num_sea += 1
                elif graph[nx][ny] and not visited[nx][ny]: #빙산이고 방문한적 없으면
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    
            
        if num_sea > 0:
            sea.append((x, y, num_sea))
            
    for x, y, num_sea in sea:
        graph[x][y] = max(0, graph[x][y] - num_sea)  #음수값 방지
        
    return 1
                    
                    


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ice = []

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))
            
            
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
year = 0
group = 0
delete = []

while ice:
    visited = [[0] * m for _ in range(n)]
    group = 0
    
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
            
        if graph[i][j] == 0:  #빙산이 바다에 잠긴 경우
            delete.append((i, j))
            
    
    if group >= 2:
        print(year)
        break
        

    ice = sorted(list(set(ice) - set(delete)))
    year += 1
    
    
if group < 2:
    print(0)
