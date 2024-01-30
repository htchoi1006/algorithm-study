n = int(input())
num = int(input())
arr = [[0]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x = n//2
y = n//2

arr[x][y] = 1
repeat = 1

i = 0
number = 2
answer = [x+1, y+1]

while x!=0 or y!=0:
    flag = 0
    
    for _ in range(2):
        for _ in range(repeat):
            
            x += dx[i]
            y += dy[i]
            arr[x][y] = number
            
            if num == number: #찾으려고 하는 수이면
                answer = [x+1, y+1]
                
            if x == 0 and y == 0:
                flag = 1
                break
                
            number += 1
            
        if flag == 1:
            break
        i = (i+1)%4
    repeat += 1
    
    
for i in arr:
    print(*i)
    
print(*answer)