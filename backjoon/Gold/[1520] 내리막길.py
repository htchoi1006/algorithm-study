n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
# n, m = 4, 5
# field = [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28], [27, 24, 22, 15, 10]]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

dp = [[-1]*m for _ in range(n)]
cnt = 0


def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    ways = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and field[x][y] > field[nx][ny]:
            ways += dfs(nx, ny)
            
    dp[x][y] = ways
    return dp[x][y]
                
                
print(dfs(0, 0))

