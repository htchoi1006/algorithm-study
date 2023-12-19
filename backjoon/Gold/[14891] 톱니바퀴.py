from collections import deque
import sys

gears = [deque(list(map(int, sys.stdin.readline().strip()))) for _ in range(4)]
gears.insert(0, [])  # 톱니바퀴 번호 인덱스를 맞추기 위해

n = int(input())
rotate = [list(map(int, input().split())) for _ in range(n)]


def rleft(gearnum, dirc, l):
    if gearnum != 1:
        if l != gears[gearnum - 1][2]:  # 서로 다른 극이었다면
            ll = gears[gearnum-1][6]
            gears[gearnum-1].rotate(dirc*(-1))
            rleft(gearnum - 1, dirc * (-1), ll)  # 왼쪽 톱니바퀴를 반대방향으로 돌림


def rright(gearnum, dirc, r):
    if gearnum != 4:
        if r != gears[gearnum + 1][6]:  # 서로 다른 극이었다면
            rr = gears[gearnum+1][2]
            gears[gearnum+1].rotate(dirc*(-1))
            rright(gearnum+1, dirc * (-1), rr)  # 오른쪽 톱니바퀴를 반대방향으로 돌림

for r in rotate:
    l = gears[r[0]][6]
    ri = gears[r[0]][2]
    gears[r[0]].rotate(r[1])
    rleft(r[0], r[1], l)
    rright(r[0], r[1], ri)

answer = 0
for i in range(1, 5):
    answer += gears[i][0]*(2**(i-1))

print(answer)