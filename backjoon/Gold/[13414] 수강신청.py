import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dt = dict()

for i in range(m):
    stu = input().rstrip()
    dt[stu] = i
    
dt = sorted(dt.items(), key = lambda x: x[1])

cnt = 0
for i in dt:
    if cnt == n:
        break
    print(i[0])
    cnt += 1
