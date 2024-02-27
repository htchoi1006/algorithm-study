n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
score.sort(key = lambda x: x[2], reverse=True)
arr = []
tmp = [0] * 101
cnt = 0

for country, player, num in score:    
    if cnt >= 3:
        break
    
    if tmp[country] < 2:
        arr.append([country, player])
        tmp[country] += 1
        cnt += 1
    else:
        continue
        
for i in arr:
    print(*i)

    

