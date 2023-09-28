n = int(input())
field = [list(map(int, input().split())) for _ in range(6)]
# field = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]
# field.sort()
# print(field)


row, col = 0, 0
big, small = 0, 0
idx_row = 0
idx_col = 0

for i in range(len(field)):    
    if(field[i][0] == 1 or field[i][0] == 2):
        if(field[i][1] > row):
            row = field[i][1]
            idx_row = i
            
    elif(field[i][0] == 3 or field[i][0] == 4):
        if(field[i][1] > col):
            col = field[i][1]
            idx_col = i
            
# print(row, col)
big = row*col

small = abs(field[(idx_row+1)%6][1] - field[(idx_row-1)%6][1]) * abs(field[(idx_col+1)%6][1] - field[(idx_col-1)%6][1])


print((big - small)*n)