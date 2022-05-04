import sys

n = int(sys.stdin.readline())

buildings = list(map(int, sys.stdin.readline().split(' ')))
sight = [0]*n


for i in range(n):
    slope = -sys.maxsize - 1
    for j in range(i+1, n):
        tmp = (buildings[j] - buildings[i]) / (j - i)
        if(tmp > slope):
            slope = tmp
            sight[i] += 1
            sight[j] += 1
            
print(max(sight))