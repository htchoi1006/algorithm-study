n = int(input())
num = list(map(int, input().split()))

visited = [1] * n

for i in range(1, n):
    for j in range(i):
        if(num[i] > num[j]):
            visited[i] = max(visited[i], visited[j]+1)


# print(visited)
print(max(visited))