from collections import deque
t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    visited = [False for _ in range(10001)]
    
    queue = deque()
    queue.append([m,''])
    visited[m] = True
    
    while queue:
        num, cmd = queue.popleft()
        
        if(num == n):
            print(cmd)
            break
            
        d = num * 2 % 10000
        if(not visited[d]):
            visited[d] = True
            queue.append([d, cmd+'D'])
            
        s = (num - 1) % 10000
        if(not visited[s]):
            visited[s] = True
            queue.append([s, cmd+'S'])
            
        l = num//1000 + (num%1000)*10
        if(not visited[l]):
            visited[l] = True
            queue.append([l, cmd+'L'])
            
        r = num//10 + (num%10)*1000
        if(not visited[r]):
            visited[r] = True
            queue.append([r, cmd+'R'])
    