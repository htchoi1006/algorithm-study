vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input()
    if pw == 'end':
        break
        
    if len(pw) == 1 and pw in vowel:
        print('<{}> is acceptable.'.format(pw))
        continue

        
    v_cnt = 0
    c_cnt = 0
    tmp = 0
    flag = True
    
    for i in range(len(pw)):
        if pw[i] in vowel:
            v_cnt += 1
            tmp += 1
            c_cnt = 0
        else:
            c_cnt += 1
            v_cnt = 0
            
        if v_cnt == 3 or c_cnt == 3:
            print('<{}> is not acceptable.'.format(pw))
            flag = False
            break
            
        if i > 0 and pw[i] == pw[i-1]:
            if pw[i] == 'e' or pw[i] == 'o':
                continue
            else:
                print('<{}> is not acceptable.'.format(pw))
                flag = False
                break
            
            
    if flag:
        if tmp == 0:
            print('<{}> is not acceptable.'.format(pw))
        else:
            print('<{}> is acceptable.'.format(pw))
        
        