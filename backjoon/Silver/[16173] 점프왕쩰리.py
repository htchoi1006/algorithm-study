n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# n = 3
# board = [[1, 1, 10], [1, 5, 1], [2, 2, -1]]
visited = [[0]*n for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] == 1:
        return
    
    if board[x][y] == -1:
        visited[x][y] = 1
        return
    
    visited[x][y] = 1
    
    dfs(x + board[x][y], y)
    dfs(x, y + board[x][y])
    
    
dfs(0, 0)
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')
    
    
            
    