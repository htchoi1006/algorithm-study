from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
# city = [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]]
house = []
chicken = []
result = 99999

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
            
            
for chi in combinations(chicken, m):
    tmp = 0
    for h in house:
        distance = 999
        for j in range(m):
            distance = min(distance, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        tmp += distance
    result = min(result, tmp)
    
print(result)