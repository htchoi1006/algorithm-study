def solution(n):
    answer = []
    
    array = [[0 for col in range(n)] for row in range(n)]
    num = 1
    x = 0; y = -1
    
    for i in range(n):
        for j in range(i, n):
            if (i % 3 == 0):
                y += 1
            
            elif (i % 3 == 1):
                x += 1
                
            elif (i % 3 == 2):
                x -= 1; y -= 1
                
            array[y][x] = num
            num += 1
    
    
    for i in range(n):
        for j in range(n):
            if (array[i][j]):
                answer.append(array[i][j])
    
    
    
    return answer