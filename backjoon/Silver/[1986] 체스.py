n, m = map(int, input().split())
chess = [[0] * m for _ in range(n)]
check = [[0] * m for _ in range(n)]

queen = list(map(int, input().split())) 
knight = list(map(int, input().split())) 
pawn = list(map(int, input().split())) 

queen = queen[1:]
knight = knight[1:]
pawn = pawn[1:]


for i in range(len(pawn)):
    if i % 2 == 0:
        chess[pawn[i]-1][pawn[i+1]-1] = 'P'
        
for i in range(len(knight)):
    if i % 2 == 0:
        chess[knight[i]-1][knight[i+1]-1] = 'K'
        
for i in range(len(queen)):
    if i % 2 == 0:
        chess[queen[i]-1][queen[i+1]-1] = 'Q'
    
# print(chess)


qdx, qdy = [0, 0, 1, -1, -1, 1, 1, -1], [1, -1, 0, 0, 1, 1, -1, -1]
kdx, kdy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]

for i in range(n):
    for j in range(m):
        if chess[i][j] == 'Q':
            check[i][j] += 1
            
            for k in range(8):
                for l in range(1, max(n, m)):
                    nx, ny = i + l*qdy[k], j + l*qdx[k]
                    
                    if not (0 <= nx < n and 0 <= ny < m) or chess[nx][ny] != 0:
                        break
                    
                    check[nx][ny] += 1
                    
        if chess[i][j] == 'K':
            check[i][j] += 1
            
            for k in range(8):
                nx, ny = i + kdx[k], j + kdy[k]
                
                if 0 <= nx < n and 0 <= ny < m and chess[nx][ny] == 0:
                    check[nx][ny] += 1
                    
                    
        if chess[i][j] == 'P':
            check[i][j] += 1
                    
                    
answer = 0

for i in range(n):
    for j in range(m):
        if check[i][j] == 0:
            answer += 1
            
            
print(answer)

print(chess)
print(check)