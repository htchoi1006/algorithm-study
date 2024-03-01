n = int(input())
num = [input() for _ in range(n)]
cnt = 0

while True:
    arr = []
    cnt -= 1
    
    for i in num:
        tmp = i[cnt:]
        if tmp in arr:
            continue
        else:
            arr.append(tmp)
        
    if len(arr) == n:
        break
        
print(len(arr[0]))
    
