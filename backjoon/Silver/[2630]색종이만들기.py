n = int(input())
papers = []

for _ in range(n):
    row = list(map(int, input().split()))
    papers.append(row)


blue, white = 0, 0

def check(row, col, n):
    global blue, white

    curr = papers[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            if(curr != papers[i][j]):
                nextt = n//2
                check(row, col, nextt)
                check(row, col + nextt, nextt)
                check(row + nextt, col, nextt)
                check(row + nextt, col + nextt, nextt) 
                return

        
    if(curr == 0):
        white += 1
    
    else:
        blue += 1
    
    return


check(0, 0, n)
print(white)
print(blue)