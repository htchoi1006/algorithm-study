a, p = map(int, input().split())
# a = 57; p = 2

arr = []
arr.append(a)
# print(arr)

tmp = 0
for i in arr:
    num = str(arr[-1])
    tmp = 0
    for j in num:
        tmp += (int(j) ** p)
#     print(tmp)
    
    if tmp in arr:
        break
    else:
        arr.append(tmp)
        
        
cnt = 0
for i in arr:
    if i == tmp:
        print(cnt)
    else:
        cnt += 1
        