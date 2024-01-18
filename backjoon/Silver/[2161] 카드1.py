from collections import deque

n = int(input())
# n = 7
cards = deque([i for i in range(1, n+1)])
out = []

# print(cards)

while cards:
    out.append(cards.popleft())
    if len(cards) != 0:
        cards.append(cards.popleft())
    
print(*out)