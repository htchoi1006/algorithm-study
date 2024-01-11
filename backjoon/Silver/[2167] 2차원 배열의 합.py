import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# n, m = 2, 3
# arr = [[1, 2, 4], [8, 16, 32]]
arr = [list(map(int, input().split())) for _ in range(n)]



t = int(input())


for _ in range(t):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    
    ans = 0
    for i in range(a, x):
        for j in range(b, y):
            ans += arr[i][j]
            
    print(ans)