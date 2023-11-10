from collections import deque

n = int(input())
standard = list(map(int, input().split()))
standard = deque(standard)
reversed_standard = []

for i in standard:
    if i == 1:
        r = 3
    elif i == 2:
        r = 4
    elif i == 3:
        r = 1
    elif i == 4:
        r = 2
    reversed_standard.append(r)
    
reversed_standard.reverse()
reversed_standard = deque(reversed_standard)
candidate = []

for _ in range(n):
    standard.rotate(1)
    reversed_standard.rotate(1)
    
    candidate.append(list(standard))
    candidate.append(list(reversed_standard))
    
answer = []



m = int(input())
for _ in range(m):
    example = list(map(int, input().split()))
    if example in candidate:
        answer.append(example)
        
print(len(answer))
for i in answer:
    print(*i)

