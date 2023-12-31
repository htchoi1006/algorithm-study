from itertools import permutations
from copy import deepcopy

n, m, k = map(int, input().split())
# n, m, k = 5, 6, 2
num = [list(map(int, input().split())) for _ in range(n)]
# num = [[1, 2, 3, 2, 5, 6], [3, 8, 7, 2, 1, 3], [8, 2, 3, 1, 4, 5], 
#        [3, 4, 5, 1, 1, 1], [9, 3, 2, 1, 4, 3]]
rcs = [list(map(int, input().split())) for _ in range(k)]
# rcs = [[3, 4, 2], [4, 2, 1]]

ans = 99999999

for p in permutations(rcs, k):
    copy = deepcopy(num)
    for r, c, s in p:
        r -= 1
        c -= 1
        
        for i in range(s, 0, -1):
            tmp = copy[r-i][c+i]
            copy[r-i][c-i+1 : c+i+1] = copy[r-i][c-i : c+i] #오른쪽
            
            for row in range(r-i, r+i): #위쪽
                copy[row][c-i] = copy[row+1][c-i]
                
            copy[r+i][c-i : c+i] = copy[r+i][c-i+1 : c+i+1] #왼쪽
            
            for row in range(r+i, r-i, -1): #아래쪽
                copy[row][c+i] = copy[row-1][c+i]
                
            copy[r-i+1][c+i] = tmp
            
    
    for i in copy:
        ans = min(ans, sum(i))
        
print(ans)
