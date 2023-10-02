w, h = map(int, input().split())
n = int(input())

def get_distance(x, y):
    if(x == 1): #북
        return y
    elif(x == 2): #남
        return w + h + w - y
    elif(x == 3): #서
        return w + h + w + h - y
    else: #동
        return w + y
    

course = []
for _ in range(n+1):
    x, y = map(int, input().split())
    course.append(get_distance(x, y))
    
answer = 0



for i in range(n):
    in_course = abs(course[-1] - course[i])
    out_course = 2 * (w + h) - in_course  #반대 방향이 더 빠를 수도 있으므로
    answer += min(in_course, out_course)
    
print(answer)