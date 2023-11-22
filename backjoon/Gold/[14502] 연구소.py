from collections import deque


n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
# lab = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
tmp = [[0] * m for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
result = 0

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                queue.append((nx, ny))
                tmp[nx][ny] = 2
                
                
def makewall(cnt):
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = lab[i][j]
                if tmp[i][j] == 2:
                    queue.append((i, j))
        bfs()

        area = 0
        global result

        for i in range(n):
            area += tmp[i].count(0)
        result = max(result, area)
        return
        
        
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makewall(cnt + 1)
                lab[i][j] = 0

makewall(0)
print(result)