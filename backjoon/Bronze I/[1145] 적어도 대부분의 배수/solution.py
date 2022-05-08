nums = list(map(int, input().split()))
n = min(nums)

while(True):
    cnt = 0
    for i in range(len(nums)):
        if(n % nums[i] == 0):
            cnt += 1
    
    if(cnt > 2):
        break
    
    n += 1
    
print(n)