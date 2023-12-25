from collections import deque

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 전체 치즈 개수 세기
for i in range(n):
    cnt += sum(cheese[i])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 1


def bfs():
    queue = deque([(0, 0)])
    melt = deque([])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                
                if cheese[nx][ny] == 0:
                    queue.append((nx, ny))
                elif cheese[nx][ny] == 1:
                    melt.append((nx, ny))
                    
    for x, y in melt:
        cheese[x][y] = 0
    return len(melt)



while True:
    visited = [[0]*m for _ in range(n)]
    meltCnt = bfs()
    cnt -= meltCnt
    
    if cnt == 0:
        print(time, meltCnt, sep='\n')
        break
        
    time += 1
    


        
