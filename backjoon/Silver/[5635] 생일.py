n = int(input())
student = []
for _ in range(n):
    n, d, m, y = input().split()
    student.append([n, int(d), int(m), int(y)])
    

student.sort(key=lambda x: (x[3], x[2], x[1], x[0]))
print(student[-1][0])
print(student[0][0])