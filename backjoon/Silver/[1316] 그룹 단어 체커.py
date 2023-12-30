n = int(input())
ans = 0

for _ in range(n):
    word = list(input())
    tmp = []
    cnt = 0
    
    for i in word:
        if not tmp:
            tmp.append(i)
            cnt += 1
#             print(1)
        elif tmp and i in tmp and i != tmp[-1]:
#             print(2)
            cnt = 0
            break
        elif tmp and i == tmp[-1]:
            continue
#             print(3)
        elif i not in tmp:
            cnt += 1
            tmp.append(i)
#             print(4)
            
    if cnt > 0:
        ans += 1
            
#     print('cnt = ', cnt)
        
print(ans)