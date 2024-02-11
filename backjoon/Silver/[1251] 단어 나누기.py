word = list(input())
tmp = []
ans = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a+b+c)
#         print(tmp)

for i in tmp:
    ans.append(''.join(i))
    
print(sorted(ans)[0])