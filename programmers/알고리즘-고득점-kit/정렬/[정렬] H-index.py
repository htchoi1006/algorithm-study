def solution(citations):
    answer = []
    n = len(citations)
    
    for h in range(0, n+1):  #h를 0부터 n까지 
        cnt = 0
        for j in range(n):   #citations 원소 하나씩 검사하기 위함
            if citations[j] >= h:  #인용 수가 h보다 크면 카운트 +1
                cnt += 1

            if cnt >= h:  #h번 이상 인용된 논문이 h편 이상이면
                if n - cnt <= h:  #나머지 논문이 h번 이하 인용되었으면
                    answer.append(h)  #answer 배열에 추가
                    
    return max(answer)
        
    

    
    