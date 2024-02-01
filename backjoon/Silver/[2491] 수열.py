n = int(input())
arr = list(map(int, input().split()))

mincnt = 0
maxcnt = 0

mintmp = 0
maxtmp = 0


for i in range(1, n):
    if arr[i] >= arr[i-1]:
        maxtmp += 1
        maxcnt = max(maxcnt, maxtmp)
    else:
        maxcnt = max(maxcnt, maxtmp)
        maxtmp = 0
        
    if arr[i] <= arr[i-1]:
        mintmp += 1
        mincnt = max(mincnt, mintmp)

    else:
        mincnt = max(mincnt, mintmp)
        mintmp = 0
        
        

print(max(maxcnt+1, mincnt+1))
    
    