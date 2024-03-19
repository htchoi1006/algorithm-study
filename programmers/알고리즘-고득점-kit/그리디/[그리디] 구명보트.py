def solution(people, limit):
    people.sort()
    boat = len(people)
    
    i = 0  #왼쪽 인덱스
    j = len(people) - 1   #오른쪽 인덱스
    
    while i < j:
        weight = people[i] + people[j]  #둘이 합친 무게
        if weight <= limit:             #limit보다 작으면, 즉 보트에 탈 수 있으면
            i += 1      #왼쪽 인덱스 1 증가
            j -= 1      #오른쪽 인덱스 1 감소
            boat -= 1   #필요한 보트 1개 감소
        else:  #둘이 합친 무게가 limit보다 크면
            j -= 1      #오른쪽 인덱스만 1 감소
            
    
    return boat
                
            
        