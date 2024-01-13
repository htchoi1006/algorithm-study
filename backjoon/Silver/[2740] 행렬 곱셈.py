N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(M)]

# N, M = 3, 2
# M, K = 2, 3
# arr1 = [[1, 2], [3, 4], [5, 6]]
# arr2 = [[-1, -2, 0], [0, 0, 3]]

ans = [[0] * K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            ans[n][k] += arr1[n][m] * arr2[m][k]
            

            
for i in range(N):
    for j in range(K):
        print(ans[i][j], end=' ')
    print()
    
            
        

