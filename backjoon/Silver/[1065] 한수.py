n = int(input())
cnt = 0

for i in range(1, n+1):
    nlist = list(map(int, str(i)))
    if i < 100:
        cnt += 1
    else:
        if nlist[0] - nlist[1] == nlist[1] - nlist[2]:
            cnt += 1
        else:
            continue
            
print(cnt)
        
