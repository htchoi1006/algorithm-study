# sudoku = [[1, 0, 3, 0, 0, 0, 5, 0, 9], [0, 0, 2, 1, 0, 9, 4, 0, 0], [0, 0, 0, 7, 0, 4, 0, 0, 0], [3, 0, 0, 5, 0, 2, 0, 0, 6], [0, 6, 0, 0, 0, 0, 0, 5, 0], [7, 0, 0, 8, 0, 3, 0, 0, 4], [0, 0, 0, 4, 0, 1, 0, 0, 0], [0, 0, 9, 2, 0, 5, 8, 0, 0], [8, 0, 4, 0, 0, 0, 1, 0, 7]]
sudoku = [list(map(int, input())) for _ in range(9)]
zero = []


def dfs(idx):
    if idx == len(zero):
        for i in range(9):
            print(''.join(map(str, sudoku[i])))
        return True
    
    i, j = zero[idx][0], zero[idx][1]
    total_num = set([num for num in range(1, 10)])
#     print('total', total_num)
    
    used = set(sudoku[i] + 
               [sudoku[r][j] for r in range(9)] + 
               [sudoku[r][c] for r in range(3*(i//3), 3*(i//3)+3) for c in range(3*(j//3), 3*(j//3)+3)])
#     print('used', used)
    
    for num in sorted(total_num - used):
#         print('num', num)
        sudoku[i][j] = num
        if dfs(idx + 1):
            return True
        sudoku[i][j] = 0
    return False



for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i, j))

dfs(0)
            