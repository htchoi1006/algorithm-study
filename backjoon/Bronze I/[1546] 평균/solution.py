n = int(input())
score = list(map(int, input().split()))
average = 0

maxscore = max(score)
for i in range(n):
    score[i] = (score[i]/maxscore) * 100
    average += score[i]
    
print(average/n)