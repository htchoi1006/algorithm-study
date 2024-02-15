n, m = map(int, input().split())
floor = [list(input()) for _ in range(n)]


row = 0
col = 0
for i in range(n):
    cnt = 0
    for j in range(m):
        if floor[i][j] == '-':
            if j == m-1:
                row += 1
            else:
                cnt += 1
        elif floor[i][j] != '-' and cnt > 0:
            cnt = 0
            row += 1
        else:
            continue
            

    
    
for i in range(m):
    cnt = 0
    for j in range(n):
        if floor[j][i] == '|':
            if j == n-1:
                col += 1
            else:
                cnt += 1
        elif floor[j][i] != '|' and cnt > 0:
            cnt = 0
            col += 1
        else:
            continue
            
print(row + col)
        
            
    
