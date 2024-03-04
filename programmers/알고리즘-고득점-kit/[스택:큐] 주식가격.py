def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n):
        cnt = 0
        flag = 1

        for j in range(i+1, n): 
            if prices[i] > prices[j]:  #만약 가격이 떨어지면
                answer.append(j-i)     #가격을 유지한 만큼의 시간을 리스트에 추가
                flag = 0
                break
            else:    #가격 안떨어지면
                cnt += 1  #시간 + 1
                
        if flag:
            answer.append(cnt)  #가격을 유지한 만큼의 시간을 리스트에 추가
                
    
    return answer