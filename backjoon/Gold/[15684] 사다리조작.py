def check():
    for start in range(n):
        now = start
        
        for j in range(h):
            if board[j][now]:
                now += 1
            elif now > 0 and board[j][now-1]:
                now -= 1
            
        if now != start:
            return False
    return True


def dfs(cnt, x, y):
    global ans
    
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
            
        for j in range(now, n-1):
            if not board[i][j] and not board[i][j+1]:
                if j > 0 and board[i][j-1]:
                    continue
                board[i][j] = True
                dfs(cnt+1, i, j+2)
                board[i][j] = False
                



n, m, h = map(int, input().split())
board = [[False]*n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a-1][b-1] = True
    
ans = 4
dfs(0, 0, 0)

if ans < 4:
    print(ans)
else:
    print(-1)


    
    