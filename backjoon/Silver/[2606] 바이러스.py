n = int(input())
v = int(input())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]
#     print(graph)
    
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            
dfs(1)
print(sum(visited) - 1)
# print(visited)