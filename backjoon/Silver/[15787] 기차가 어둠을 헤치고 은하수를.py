from collections import deque

n, m = map(int, input().split())
train = [deque([0] * 20) for _ in range(n)]

for _ in range(m):
    cmd = list(map(int, input().split()))
    
    if(cmd[0] == 1):
        train[cmd[1]-1][cmd[2]-1] = 1
    elif(cmd[0] == 2):
        train[cmd[1]-1][cmd[2]-1] = 0
    elif(cmd[0] == 3):
        train[cmd[1]-1].rotate(1)
        train[cmd[1]-1][0] = 0
    else:
        train[cmd[1]-1].rotate(-1)
        train[cmd[1]-1][19] = 0
        
answer = []

for i in train:
    if(i not in answer):
        answer.append(i)
        
print(len(answer))