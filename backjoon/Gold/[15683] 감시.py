import copy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
# office = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 6, 0], [0, 0, 0, 0, 0, 0]]
cctv = []

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [0, 3], [1, 2], [2, 3]],
    [[0, 1, 2], [1, 2, 3], [0, 1, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

#북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

            
def fill(office, mode, x, y):
    for i in mode:
        nx = x
        ny = y
        
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if office[nx][ny] == 6:
                break
            elif office[nx][ny] == 0:
                office[nx][ny] = -1
                

def dfs(depth, office):
    global min_val
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += office[i].count(0)
        
        min_val = min(min_val, count)
        return
    
    tmp = copy.deepcopy(office)
    cctv_num, x, y = cctv[depth]
    
    for i in mode[cctv_num]:
        fill(tmp, i, x, y)
        dfs(depth + 1, tmp)
        tmp = copy.deepcopy(office)
        
        
        

for i in range(n):
    for j in range(m):
        if office[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([office[i][j], i, j])
            

min_val = 999999999
dfs(0, office)
print(min_val)
        