def solution(n, times):
    left = 1  #최소 숫자
    right = max(times) * n  #최대 숫자
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2  
        num = 0 
        
        for time in times:
            num += mid//time  #최대로 심사받을 수 있는 사람의 수
            
            if num >= n:  #중간에 심사받을 수 있는 사람의 수가 주어진 사람의 수보다 많아지면 break
                break

        if num >= n:   #심사받을 수 있는 사람의 수가 주어진 사람의 수보다 많으면 시간이 충분하다는 뜻
            right = mid - 1   #최대 시간 줄이기
            ans = mid
            
        else:   #심사받을 수 있는 사람의 수가 주어진 사람의 수보다 적으면 시간이 부족하다는 뜻
            left = mid + 1   #최소 시간 늘리기
        
            
                
    return ans