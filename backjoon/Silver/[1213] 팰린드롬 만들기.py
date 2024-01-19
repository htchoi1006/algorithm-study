import collections 

items = list(input())
# items = ['A', 'A', 'B', 'B']
dic = collections.Counter(items)

cnt = 0
mid = ''
ans = ''


for i, j in list(dic.items()):
    if j % 2 == 1: #홀수
        cnt += 1
        mid = i
        
        if cnt >= 2:
            break



if cnt < 2:
    for i, j in sorted(dic.items()):
        ans += i * (j//2)
    print(ans + mid + ans[::-1])

else:
    print("I'm Sorry Hansoo")