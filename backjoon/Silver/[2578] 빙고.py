bingo = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    num += list(map(int, input().split()))

# bingo = [[11, 12, 2, 24, 10], [16, 1, 13, 3, 25], [6, 20, 5, 21, 17], [19, 4, 8, 14, 9], [22, 15, 7, 23, 18]]
# num = [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]

                
            
def check():
    bingo_count = 0
    
    for i in bingo:
        if i.count(0) == 5:
            bingo_count += 1

            
    for i in range(5):
        tmp = 0
        for j in range(5):
            if bingo[j][i] == 0:
                tmp += 1
        if tmp == 5:
            bingo_count += 1

    
    d1 = 0        
    for i in range(5):
        if bingo[i][i] == 0:
            d1 += 1
    if d1 == 5:
        bingo_count += 1

    d2 = 0     
    for i in range(5):
        if bingo[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        bingo_count += 1

                
    return bingo_count
            
    
    
cnt = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if num[i] == bingo[x][y]:
                bingo[x][y] = 0
                cnt += 1
                
            
    if cnt >= 12:
        result = check()
        
        if result >= 3:
            print(i+1)
            break
            

        

        