c, p = map(int,input().split())
fd = list(map(int, input().split()))
ans = 0

if p == 1:
    ans += c #세우는 경우
    for i in range(c-3): #눕히는 경우
        if fd[i] == fd[i+1] and fd[i+1] == fd[i+2] and fd[i+2] == fd[i+3]:
            ans += 1
            
            
if p == 2:
    for i in range(c-1):
        if fd[i] == fd[i+1]:
            ans += 1
            
if p == 3:
    for i in range(c-2): #눕히는 경우(001)
        if fd[i] == fd[i+1] and fd[i+1] == fd[i+2]-1:
            ans += 1
            
    for i in range(c-1): #세우는 경우 (10)
        if fd[i] == fd[i+1]+1:
            ans += 1
            
            
if p == 4:
    for i in range(c-2):
        if fd[i]-1 == fd[i+1] and fd[i+1] == fd[i+2]:
            ans += 1

    for i in range(c-1):
        if fd[i]+1 == fd[i+1]:
            ans += 1
            
            
if p == 5:
    for i in range(c-2):
        if fd[i] == fd[i+1] and fd[i+1] == fd[i+2]:
            ans += 1
        if fd[i]-1 == fd[i+1] and fd[i+1] == fd[i+2]-1:
            ans += 1
            
    for i in range(c-1):
        if fd[i]-1 == fd[i+1]:
            ans += 1
        if fd[i]+1 == fd[i+1]:
            ans += 1
            
            
if p == 6:
    for i in range(c-2):
        if fd[i] == fd[i+1] and fd[i+1] == fd[i+2]:
            ans += 1
        if fd[i]+1 == fd[i+1] and fd[i+1] == fd[i+2]:
            ans += 1
    
    for i in range(c-1):
        if fd[i] == fd[i+1]:
            ans += 1
        if fd[i]-2 == fd[i+1]:
            ans += 1
            
            
if p == 7:
    for i in range(c-2):
        if fd[i] == fd[i+1] and fd[i+1] == fd[i+2]:
            ans += 1
        if fd[i] == fd[i+1] and fd[i+1]-1 == fd[i+2]:
            ans += 1
            
    for i in range(c-1):
        if fd[i] == fd[i+1]:
            ans += 1
        if fd[i]+2 == fd[i+1]:
            ans += 1
            
            
            
print(ans)
    