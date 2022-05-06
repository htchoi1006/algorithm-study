def calculation(n):
    tmp = n//10 + n%10
    tmp = (n%10)*10 + tmp%10
    return tmp



n = int(input())
cnt = 0
answer = n
while(True):
    answer = calculation(answer)
    cnt += 1
    if(answer == n):
        break
        
print(cnt)
