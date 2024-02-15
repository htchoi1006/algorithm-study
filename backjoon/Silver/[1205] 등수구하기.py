import sys
input = sys.stdin.readline

n, taesu, p = map(int, input().split())
score = list(map(int, input().split()))

# n, score, p = 3, 90, 10
# rank = [100, 90, 80]

if n == 0:
    print(1)
    exit()

cnt = 0
rank = 1

for i in score:
    if i > taesu:
        cnt += 1
        rank += 1
    elif i == taesu:
        cnt += 1
    else:
        break
        
# print(cnt, rank)
        
if cnt < p:
    print(rank)
else:
    print(-1)