s = int(input())
switch = list(map(int, input().split()))
n = int(input())
# s = 8
# switch = [0, 1, 0, 1, 0, 0, 0, 1]
# n = 2


switch.insert(0, 0)


def change(index):
    if switch[index] == 0:
        switch[index] = 1
    elif switch[index] == 1:
        switch[index] = 0
        

for _ in range(n):
    gender, index = map(int, input().split())
    cnt = 0
    
    if gender == 1: #남학생
        for i in range(index, s+1, index):
            change(i)
                
                
    elif gender == 2: #여학생
        for i in range(1, min(index-1, s-index)+1):
            if switch[index-i] != switch[index+i]:
                break
            else:    
                cnt += 1
                
        for i in range(index-cnt, index+cnt+1):
            change(i)
                

                    
switch.pop(0)

# print(switch)
if len(switch) < 21:
    print(*switch)
else:
    print('\n'.join(' '.join(map(str, switch[i:i+20])) for i in range(0, len(switch), 20)))
        