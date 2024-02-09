n, m = map(int, input().split())
j = int(input())
apple = [int(input()) for _ in range(j)]

# n, m = 5, 1
# j = 3
# apple = [1, 5, 3]

now = 1
ans = 0
for i in range(j):
    if apple[i] < now:
        ans += now - apple[i]
        now -= (now - apple[i])
    elif apple[i] > now + m - 1:
        ans += apple[i] - (now + m - 1)
        now += (apple[i] - (now + m - 1))
    else:
        continue
        
print(ans)
    