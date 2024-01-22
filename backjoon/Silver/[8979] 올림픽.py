n, target = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]


# n, target = 4, 3
# country = [[2, 0, 1, 0], [1, 1, 2, 0], [3, 0, 1, 0], [4, 0, 0, 1]]


country.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

idx = [country[i][0] for i in range(n)].index(target)

for i in range(n):
    if country[idx][1:] == country[i][1:]:
        print(i+1)
        break