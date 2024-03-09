def solution(brown, yellow):
    answer = []
    
    #(노란색 가로개수 * 2) + (노란색 세로개수 * 2) + 4 == 갈색 전체 개수 
    
    for i in range(1, yellow+1):  
        if yellow%i == 0:  #나누어 떨어지는 수로 노란색의 가로개수, 세로개수 설정하기
            width = int(yellow/i)  
            height = i
            
            if width*2 + height*2 + 4 == brown:  #위 공식을 만족하면 answer 배열에 추가
                answer.append(width+2)
                answer.append(height+2)
                
                break

    
    return answer