N, L = map(int, input().split())
pipe = sorted(list(map(int, input().split())))

end = pipe[0] -1 + L 
result = 1

for i in range(0,N):
    if(end >= pipe[i]):
        continue
    else:
        result += 1
        end = pipe[i] -1 + L 
        
        
print(result)