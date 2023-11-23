n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
# room = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
visited = [[0] * m for _ in range(n)]
visited[r][c] = 1
cnt = 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    flag = 0
    
    for i in range(4):
        d = (d+3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                
                r = nx
                c = ny
                flag = 1
                break
        
    if flag == 0:
        if room[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        else:
            r -= dx[d]
            c -= dy[d]
            
