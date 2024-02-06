w, h = map(int, input().split())
t = int(input())
# w, h = 10, 8
# t = 3

paper = [[0]*h for _ in range(w)]
width = [0, w]
height = [0, h]

for _ in range(t):
    a, b = map(int, input().split())
    if a == 0:
        height.append(b)
    elif a == 1:
        width.append(b)
        
        
width.sort(reverse=True)
height.sort(reverse=True)
ans = 0

for i in range(len(width)-1):
    for j in range(len(height)-1):
        x = width[i] - width[i+1]
        y = height[j] - height[j+1]
        
        ans = max(ans, x*y)
        
print(ans)
    
