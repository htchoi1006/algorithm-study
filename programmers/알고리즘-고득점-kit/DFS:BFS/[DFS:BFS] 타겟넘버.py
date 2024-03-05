def solution(numbers, target):
    n = len(numbers)  
    answer = 0
    
    def dfs(idx, result):
        if idx == n:  #마지막 원소까지 갔으면
            if result == target:  #내가 구하고자 하는 숫자가 나왔을 경우
                nonlocal answer   
                answer += 1  #정답 개수에 1 추가
            return
        else:
            dfs(idx+1, result+numbers[idx])   #인덱스 1추가, result에 현재 수 더해줌
            dfs(idx+1, result-numbers[idx])   #인덱스 1추가, result에 현재 수 빼줌
            
    dfs(0, 0)
        
    
    return answer