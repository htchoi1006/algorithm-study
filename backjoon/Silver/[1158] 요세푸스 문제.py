from collections import deque

n, k = map(int, input().split())
circle = [i for i in range(1, n+1)]
queue = deque(circle)
result = []

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
#         print(queue)
        
    
    result.append(queue.popleft())
#     print(result)

print(str(result).replace('[', '<').replace(']', '>'))
