n, m = map(int, input().split())
s = []
num = list(map(int, input().split()))
num.sort()

def dfs(start):
    if(len(s) == m):
#         print(' '.join(map(str, s)))
        print(*s)
        return
    
    for i in range(start, n):
#         if(num[i] not in s):
        s.append(num[i])
        dfs(i)
        s.pop()
            
            
dfs(0)