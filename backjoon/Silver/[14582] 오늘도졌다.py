team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

# team1 = [1, 0, 0, 0, 0, 0, 2, 2, 1]
# team2 = [0, 0, 3, 0, 0, 0, 0, 1, 4]
score1, score2 = 0, 0
flag = False

for i in range(9):
    score1 += team1[i]
    if score1 > score2:
        flag = True
    score2 += team2[i]
    
    
    
if flag and score1 < score2:
    print('Yes')
else:
    print('No')

