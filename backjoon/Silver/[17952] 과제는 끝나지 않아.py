import sys
input = sys.stdin.readline

t = int(input())
score = 0
tmp = []

for i in range(t):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        if cmd[2] == 1:
            score += cmd[1]
        else:
            tmp.append([cmd[1], cmd[2]-1])
        continue
            
    
    if tmp:
        tmp[-1][1] -= 1
        if tmp[-1][1] == 0:
            score += tmp[-1][0]
            tmp.pop()
            
            
print(score)            
    