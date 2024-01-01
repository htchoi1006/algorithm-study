from collections import deque

n, m = map(int, input().split())
# n, m = 6, 4
graph = [list(map(int, input())) for _ in range(n)]
# graph = [[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    
    while queue:
        a, b, c = queue.popleft()
        
        if a == n-1 and b == m-1: #끝점 도달
            return visited[a][b][c]
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            #다음 이동할 곳이 벽이고, 벽 파괴 한번도 안쓴 경우
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            
            #다음 이동할 곳이 벽이 아니고, 아직 방문 안한 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
                
    return -1


print(bfs(0, 0, 0))
        
        
        
        
        