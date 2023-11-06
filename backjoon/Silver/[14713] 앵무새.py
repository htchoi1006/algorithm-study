n = int(input())
bird = [list(input().split()) for _ in range(n)]
answer = list(map(str, input().split()))


for item in answer:
    correct = False
    for i in range(n):
        if(len(bird[i]) != 0):
            if item == bird[i][0]:
                bird[i].pop(0)
                correct = True
                break
    
    if correct == False:
        break
        

left = 0
for line in bird:
    left += len(line)
    
if correct and left == 0:
    print("Possible")
else:
    print("Impossible")