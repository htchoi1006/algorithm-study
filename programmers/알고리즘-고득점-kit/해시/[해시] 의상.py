def solution(clothes):
    answer = 1
    
    dic = {i:[] for _, i in clothes}  #카테고리:리스트 로 이루어진 딕셔너리 생성
    for item, category in clothes:
        dic[category].append(item)    #카테고리에 아이템 담기
        
    for i in dic.values():  
        answer *= (len(i)+1)  #옷을 하나만 입는 경우 짝맞출 가짜 옷을 카운팅
        
    
    return answer - 1  #가짜 옷끼리 조합되는 한 가지 경우를 제외