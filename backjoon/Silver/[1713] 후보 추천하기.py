n = int(input())
num = int(input())
student = list(map(int, input().split()))

candidate = []
recommend = []

for i in range(num):
    if(student[i] in candidate):
        for j in range(len(candidate)):
            if(student[i] == candidate[j]):
                recommend[j] += 1
            
    else:
        if(len(candidate) >= n):
            for j in range(n):
                if(recommend[j] == min(recommend)):
                    del candidate[j]
                    del recommend[j] 
                    break
            
        candidate.append(student[i])
        recommend.append(1)
    
candidate.sort()
print(*candidate)
                
                
    