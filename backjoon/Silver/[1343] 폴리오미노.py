board = list(input())
# board = ['X', 'X', 'X', 'X', 'X', 'X', '.', 'X', 'X']

xcnt = 0
ans = ''
for i in board:
    if i == 'X':
        xcnt += 1
    if i == '.':
        if xcnt%2 == 1:
            print(-1)
            exit(0)
        else:
            ans += 'AAAA'*(xcnt//4) 
#             xcnt //= 4
            ans += 'BB'*(xcnt%4//2) 
            xcnt = 0

        ans += '.'
        
        

if xcnt%2 == 1:
    print(-1)
    exit(0)
else:
    ans += 'AAAA'*(xcnt//4) 
    ans += 'BB'*(xcnt%4//2) 
    print(ans)
            