n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
# a = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]

for i in range(1, n):
    a[i][0] += min(a[i-1][1], a[i-1][2]) 
    a[i][1] += min(a[i-1][0], a[i-1][2])
    a[i][2] += min(a[i-1][0], a[i-1][1])
    
print(min(a[n-1][0], a[n-1][1], a[n-1][2]))
    