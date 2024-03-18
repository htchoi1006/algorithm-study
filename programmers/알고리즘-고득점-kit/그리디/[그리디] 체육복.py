def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:  #lost와 reserve에 중복되는 원소 제거
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
            
    
    for i in reserve:  
        if i-1 in lost:  #여벌의 체육복을 가진 학생 바로 앞 학생이면
            lost.remove(i-1)
        elif i+1 in lost:   #여벌의 체육복을 가진 학생 바로 뒤 학생이면
            lost.remove(i+1)
            
    return n-len(lost)