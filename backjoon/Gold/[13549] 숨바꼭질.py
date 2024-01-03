from collections import deque

n, k = map(int, input().split())
time = [0] * 100001


def bfs(x, y):
    queue = deque()
    if x == 0:
        queue.append(1)
    else:
        queue.append(x)
        
    while queue:
        x = queue.popleft()
        if y == x:
            return time[x]
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < 100001 and time[nx] == 0:
                if nx == x*2:
                    time[nx] = time[x]
                    queue.appendleft(nx)
                else:
                    time[nx] = time[x] + 1
                    queue.append(nx)
        
        

if n == 0:
    print(bfs(n, k) + 1)
else:
    print(bfs(n, k))
