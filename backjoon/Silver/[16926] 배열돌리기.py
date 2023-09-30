from collections import deque

n, m, r = map(int, input().split())
nums = [list(input().split()) for _ in range(n)]
answer = [[0]*m for _ in range(n)]
queue = deque()

loops = min(n, m)//2

for i in range(loops):
    queue.clear()
    queue.extend(nums[i][i:m-i]) #위쪽
    queue.extend([row[m-i-1] for row in nums[i+1:n-i-1]]) #오른쪽
    queue.extend(nums[n-i-1][i:m-i][::-1]) #아래쪽
    queue.extend([row[i] for row in nums[i+1:n-i-1][::-1]]) #왼쪽
    
#     print(*queue)
    
    queue.rotate(-r)
    
#     print(*queue)
    
    for j in range(i, m-i):
        answer[i][j] = queue.popleft()
    for j in range(i+1, n-i-1):
        answer[j][m-i-1] = queue.popleft()
    for j in range(m-i-1, i-1, -1):
        answer[n-i-1][j] = queue.popleft()
    for j in range(n-i-2, i, -1):
        answer[j][i] = queue.popleft()
        
        
for line in answer:
    print(" ".join(line))
    
