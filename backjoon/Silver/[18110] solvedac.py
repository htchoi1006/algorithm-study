import sys


input = sys.stdin.readline

def newRound(val):
    if val - int(val) >= 0.5:
        return int(val) + 1
    else:
        return int(val)

n = int(input())


if n:
    rate = [int(input()) for _ in range(n)]
    rate.sort()
    x = newRound(n * 0.15)
    print(newRound(sum(rate[x:-x] if x else rate) / (n - 2*x)))
    
else:
    print(0)