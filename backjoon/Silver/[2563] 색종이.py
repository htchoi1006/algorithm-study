import math

n = int(input())
paper = [[0] * 100 for _ in range(100)]
ans = 0

for _ in range(n):
    y, x = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
            
    
for i in range(100):
    ans += paper[i].count(1)
    
print(ans)