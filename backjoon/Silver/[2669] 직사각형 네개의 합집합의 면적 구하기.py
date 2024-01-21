# square = [list(map(int, input().split())) for _ in range(4)]
# square = [[1, 2, 4, 4], [2, 3, 5, 7], [3, 1, 6, 5], [7, 3, 8, 6]]
index = [[0]*101 for _ in range(101)]

for _ in range(4):
    w, x, y, z = map(int, input().split())
    
    for i in range(x, z):
        for j in range(w, y):
            if index[i][j] == 0:
                index[i][j] = 1
            
            
ans = 0

for i in range(101):
    ans += index[i].count(1)
    
print(ans)