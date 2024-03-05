def solution(progresses, speeds):
    answer = [] #정답을 담는 리스트
    tmp = []    #100퍼센트까지 되려면 몇 분 일해야하는지 담는 리스트
    
    for i in range(len(progresses)):  #100퍼센트까지 일하려면 몇 분 일해야하는지 계산
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt += 1
        tmp.append(cnt)
        
        
    max_num = tmp[0]
    cnt = 1
    for i in range(1, len(tmp)):  
        if tmp[i] > max_num:  #현재 수가 기존 수보다 더 크면
            answer.append(cnt) #앞의 업무가 다 끝났다는 뜻
            max_num = tmp[i]
            cnt = 1
        else:
            cnt += 1  #앞의 업무가 아직 안끝났다는 뜻
            continue
            
            
    answer.append(cnt)
    return answer