import sys

n = int(sys.stdin.readline())
a = []
b = []
answer = 0


for _ in range(n):
    num = int(sys.stdin.readline())
    
    if(num > 1):
        a.append(num)
    elif(num == 1):
        answer += 1
    else:
        b.append(num)
        

a.sort(reverse=True)
b.sort()


if(len(a) % 2 == 0):
    for i in range(0, len(a), 2):
        answer += a[i] * a[i+1]
else:
    for i in range(0, len(a)-1, 2):
        answer += a[i] * a[i+1]
    answer += a[-1]
    

    
if(len(b) % 2 == 0):
    for i in range(0, len(b), 2):
        answer += b[i] * b[i+1]
else:
    for i in range(0, len(b)-1, 2):
        answer += b[i] * b[i+1]
    answer += b[-1]
    
    
print(answer)