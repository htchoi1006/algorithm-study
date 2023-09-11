from itertools import combinations


def cal(a, b):
    dist = 0
    for i, j in zip(a, b):
        if(i != j):
            dist += 1
    return dist

t = int(input())

for _ in range(t):
    n = int(input())
    mbti = input().split()
    
    if(n > 32):
        print(0)
        
    else:
        res = 13
        case = combinations(mbti, 3)
        for a, b, c in case:
            dist = 0
            dist += cal(a, b)
            dist += cal(b, c)
            dist += cal(a, c)
            
            res = min(res, dist)
        print(res)