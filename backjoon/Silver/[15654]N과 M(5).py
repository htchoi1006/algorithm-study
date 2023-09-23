n, m = map(int, input().split())
s = []
num = list(map(int, input().split()))
num.sort()

def dfs(start):
    if(len(s) == m):
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if(num[i] not in s):
            s.append(num[i])
            dfs(i+1)
            s.pop()
            
            
dfs(1)