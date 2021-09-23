import sys


n = int(sys.stdin.readline())
paper = [[0]*101 for _ in range(101)]

# print(paper)
# print()



for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(10):
        for k in range(10):
            paper[a+j][b+k] = 1
    
    
cnt = 0

for i in range(100):
    for j in range(100):
        if(paper[i][j] == 1):
            if(paper[i-1][j] == 0): 
                cnt += 1
            if(paper[i][j-1] == 0):
                cnt += 1
            if(paper[i+1][j] == 0):
                cnt += 1
            if(paper[i][j+1] == 0):
                cnt += 1
                
        else:
            continue
            

print(cnt)