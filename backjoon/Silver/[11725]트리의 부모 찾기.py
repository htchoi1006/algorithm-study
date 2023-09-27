from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
queue = deque()
queue.append(1)

ans = [0]*(n+1)

def bfs():
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if(ans[i] == 0):
                ans[i] = now
                queue.append(i)
                
bfs()
res = ans[2:]

for i in res:
    print(i)