n = int(input())
room = [list(input()) for _ in range(n)]

# n = 5
# room = [['.', '.', '.', '.', 'X'], ['.', '.', 'X', 'X', '.'], ['.', '.', '.', '.', '.'], ['.', 'X', 'X', '.', '.'], ['X', '.', '.', '.', '.']]

def row(room):
    row_cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if room[i][j] == '.':
                tmp += 1
            elif room[i][j] == 'X':
                tmp = 0
            if tmp == 2:
                row_cnt += 1
                
                
    return row_cnt
    

def col(room):
    col_cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if room[j][i] == '.':
                tmp += 1
            elif room[j][i] == 'X':
                tmp = 0
            if tmp == 2:
                col_cnt += 1
                
                
    return col_cnt
                

r = row(room)
c = col(room)
print(r, c)