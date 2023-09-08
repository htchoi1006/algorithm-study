t = int(input())

for i in range(t):
    m, n, x, y = map(int, input().split())
    flag = 1
    
    while(x <= m*n):
        if((x-y)%n == 0):
            print(x)
            flag = 0
            break
        x += m
        
    if flag:
        print(-1)