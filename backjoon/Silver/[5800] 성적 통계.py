n = int(input())
# n = 2

for i in range(n):
    student = list(map(int, input().split()))
    cnt = student[0]
    student = student[1:]
    student.sort(reverse=True)
    
    gap = 0
    for j in range(cnt-1):
        tmp = student[j] - student[j+1]
        if tmp > gap:
            gap = tmp
    
    print('Class', i+1)
#     print(student)
    print('Max ' + str(student[0]) + ', Min ' + str(student[-1]) + ', Largest gap ' + str(gap))