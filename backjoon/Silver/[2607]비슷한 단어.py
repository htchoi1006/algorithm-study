n = int(input())
main_word = list(input())
answer = 0

for _ in range(n-1):
    compare = main_word[:]
    word = input()
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
            
    if(cnt < 2 and len(compare) < 2):
        answer += 1
        
print(answer)
    