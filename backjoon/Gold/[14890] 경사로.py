n, l = map(int, input().split())
floor = [list(map(int, input().split())) for _ in range(n)]

# n, l = 6, 2
# floor = [[3, 3, 3, 3, 3, 3], [2, 3, 3, 3, 3, 3], [2, 2, 2, 3, 2, 3], [1, 1, 1, 2, 2, 2], [1, 1, 1, 3, 3, 1], [1, 1, 2, 3, 3, 2]]


def check(board):
    bridge = [False for i in range(n)]
    
    for i in range(n-1):
        if board[i] == board[i+1]:
            continue
        
        if abs(board[i] - board[i+1]) >= 2: #높이가 2이상 차이나는 경우
            return False
        
        if board[i] > board[i+1]: #왼쪽이 더 높은 경우
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if board[j] != board[i+1]:
                        return False
                    if bridge[j] == True:
                        return False
                    bridge[j] = True
                else:
                    return False
                
        else: #오른쪽이 더 높은 경우
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if board[j] != board[i]:
                        return False
                    if bridge[j] == True:
                        return False
                    bridge[j] = True
                else:
                    return False
                
    return True
   
    
    
def rotate(n, arr):
    ret = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
            
    return ret
    
    
    
ans = 0
    
for i in floor:
    if check(i):
        ans += 1
        

floor = rotate(n, floor)

for i in floor:
    if check(i):
        ans += 1


print(ans)

            
            
