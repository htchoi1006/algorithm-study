n = input()
arr = []

for i in n:
    arr.append(int(i))
# print(arr)

visited = [0] * 10
# print(visited)

for i in arr:
    if i == 6 or i == 9:
        if visited[6] < visited[9]:
            visited[6] += 1
        else:
            visited[9] += 1
    else:
        visited[i] += 1

print(max(visited))

    