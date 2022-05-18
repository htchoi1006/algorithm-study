n = int(input())
students = []
tmp = [0] * n

for i in range(n):
    students.append(list(map(int,input().split())))
    tmp[i] = [0] * n
    

    
for i in range(5):
    for j in range(n):
        for k in range(j+1,n):
            if(students[j][i] == students[k][i]):
                tmp[k][j] = 1
                tmp[j][k] = 1

            

cnt = []
for i in tmp:
    cnt.append(i.count(1))
    
print(cnt.index(max(cnt)) + 1)



