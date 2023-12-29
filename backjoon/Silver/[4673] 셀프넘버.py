l = [i for i in range(1, 10001)]

for i in range(1, 10001):
    cnt = i
    while i >= 10:
        cnt += i % 10
        i //= 10
    cnt += i
    
    if cnt in l:
        l.remove(cnt) 
    

for i in l:
    print(i)
        