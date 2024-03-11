def solution(nums):
    n = len(nums)
    tmp = set(nums)
    
    return len(tmp) if len(tmp) <= n//2 else n//2
