n, k = map(int, input().split())
tmp = 0
visited = [True] * (n+1)

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if visited[j] != False:
            visited[j] = False
            tmp += 1
            
            if tmp == k:
                print(j)
