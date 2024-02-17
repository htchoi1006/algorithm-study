n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]

# n = 3
# students = [[4, 2, 5, 1, 7], [3, 1, 9, 4, 5], [9, 8, 1, 2, 3], [8, 1, 9, 3, 4], [7, 2, 3, 4, 8], [1, 9, 2, 5, 7], [6, 5, 2, 3, 4], [5, 1, 9, 2, 8], [2, 9, 3, 1, 4]]
arr = [[0]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for order in range(n**2):
    student = students[order]
    
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in student[1:]:
                            like += 1
                        if arr[nx][ny] == 0:
                            blank += 1
                            
                tmp.append([like, blank, i, j])
                
    tmp.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = student[0]
    
        

result = 0
students.sort()


for i in range(n):
    for j in range(n):
        ans = 0
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in students[arr[i][j]-1]:
                    ans += 1
                    
        if ans != 0:
            result += 10 ** (ans - 1)
            
            
print(result)
                



