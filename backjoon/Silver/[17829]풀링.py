n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

def pooling(size, x, y):
    mid = size//2
    if(size == 2):
        answer = [nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        answer.sort()
        return answer[-2]
    
    lt = pooling(mid, x, y)
    rt = pooling(mid, x+mid, y)
    lb = pooling(mid, x, y+mid)
    rb = pooling(mid, x+mid, y+mid)

    answer = [lt, rt, lb, rb]
    answer.sort()
    return answer[-2]

print(pooling(n, 0, 0))
