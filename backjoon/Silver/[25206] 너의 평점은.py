dic = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+':2.5, 'C0':2, 'D+':1.5, 'D0':1, 'F':0}
ans = 0
cnt = 0

for _ in range(20):
    name, size, grade = input().split()
#     print(name, size, grade)
    
    if grade == 'P':
        continue
        
    cnt += float(size)
    ans += float(size) * float(dic[grade])
    
num = ans/cnt
print(f"{num:.6f}")
    
    