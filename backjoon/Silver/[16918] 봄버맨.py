from collections import deque

r, c, n = map(int, input().split())

state2 = [list(input()) for _ in range(r)]
queue1 = deque()


for i in range(n):
    if i == 0:
        continue
        
    elif i % 2 == 1:
        count = 0
        for i in range(r):
            for j in range(c):
                if state2[i][j] == 'O':
                    queue1.append((i, j))
                    count += 1
                else:
                    state2[i][j] = 'O'


    elif i != 0 and i % 2 == 0:
        while queue1:
            x, y = queue1.popleft()
            state2[x][y] = '.'
            if x-1 >= 0:
                state2[x-1][y] = '.'
            if x+1 < r:
                state2[x+1][y] = '.'
            if y-1 >= 0:
                state2[x][y-1] = '.'
            if y+1 < c:
                state2[x][y+1] = '.'
            

        
                    
                    
                    

                    
                    
                    
for i in range(r):
    for j in range(c):
        print(state2[i][j], end='')
    print()
