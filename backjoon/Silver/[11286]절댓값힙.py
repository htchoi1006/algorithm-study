import heapq
import sys

t = int(input())
heap = []

for _ in range(t):
    num = int(sys.stdin.readline())
    if(num != 0):
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)