from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
num = [int(input()) for _ in range(n)]
# num = [1, 3, 8, -2, 2]
num.sort()
# print(num)

print(round(sum(num)/len(num)))
print(num[n//2])

cnt = Counter(num).most_common()

if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
    
    
    

print(num[-1] - num[0])