n = int(input())
dasom = int(input())
candidate = [int(input()) for i in range(n-1)]

# n = 5
# dasom = 5
# candidate = [10, 7, 3, 8]
candidate.sort(reverse=True)
cnt = 0

if n == 1:
    print(0)
else:
    while candidate[0] >= dasom:
        candidate[0] -= 1
        dasom += 1
        candidate.sort(reverse=True)
        cnt += 1
        
    print(cnt)
        
