a, b = map(int, input().split())
numlist = [0]
answer = 0

for i in range(1, b+1):
    for j in range(i):
        numlist.append(i)
        
for i in range(a,b+1):
    answer += numlist[i]
        

print(answer)