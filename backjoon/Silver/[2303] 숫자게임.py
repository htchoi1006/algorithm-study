n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]

# n = 3
# cards = [[7, 5, 5, 4, 9], [1, 1, 1, 1, 1], [2, 3, 3, 2, 10]]
ans = -1
num = 0
cnt = 0

for card in cards:
    cnt += 1
    tmp = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                tmp = max(tmp, ((card[i] + card[j] + card[k])%10))

    if tmp >= ans:
        num = cnt
        ans = tmp
    
        
    
# print(ans)
print(num)
