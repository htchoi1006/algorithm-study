n = input()
cnt = 0

while len(n) >= 2:
    tmp = 0
    for i in range(len(n)):
        tmp += int(n[i])
    n = str(tmp)
    cnt += 1
        

print(cnt)

if int(n) % 3 == 0:
    print('YES')
else:
    print('NO')