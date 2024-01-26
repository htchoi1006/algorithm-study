n = int(input())
a = list(map(int, input().split()))

for i in range(n-1, 0, -1):
    if a[i] < a[i-1]:
        x, y = i-1, i
        
        for j in range(n-1, 0, -1):
            if a[j] < a[x]:
                a[j], a[x] = a[x], a[j]
                a = a[:i] + sorted(a[i:], reverse=True)
                print(*a)
                exit(0)
                
print(-1)