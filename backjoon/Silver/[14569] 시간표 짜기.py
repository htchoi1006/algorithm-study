n = int(input())
classes = []
for _ in range(n):
    tmp = list(map(int, input().split()))[1:]
    classes.append(tmp)
# classes = [[1, 2, 3, 4], [5, 6, 7, 8, 9, 10], [11, 21, 31, 41]]
    
    
m = int(input())
students = []
for _ in range(m):
    tmp = list(map(int, input().split()))[1:]
    students.append(tmp)
# students = [[1, 2, 3, 4, 5, 6, 7, 8], 
#             [1, 2, 3, 7, 8, 9, 10], 
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 31, 41], 
#             [41, 42, 43, 44, 45], 
#             [1, 5, 6, 7, 8, 9, 10, 11, 21, 31]]

answer = [0] * m
    
    
for i in range(n):
    for j in range(m):
        if all(elem in students[j] for elem in classes[i]):
            answer[j] += 1
            
            
for i in answer:
    print(i)

        
    


    