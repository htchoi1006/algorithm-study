def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])  #cost가 낮은 순서대로 정렬
    link = set([costs[0][0]])  #첫번째 섬 저장
    
    while len(link) != n:  #link에 모든 섬들이 다 찰때까지 반복
        for i in costs:  
            if i[0] in link and i[1] in link:  #두 섬이 모두 link에 있을 때 continue
                continue
            if i[0] in link or i[1] in link:   #두 섬 중 하나라도 link에 없을 떄 
                link.update([i[0], i[1]])      #link에 추가 (update 함수로 중복 제거)
                answer += i[2]                 #answer 에 cost 더해주기
                break                           
        
    return answer