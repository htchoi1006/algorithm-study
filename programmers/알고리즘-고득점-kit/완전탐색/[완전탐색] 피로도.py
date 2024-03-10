from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):  #던전 도는 순서 순열로 만듦
        k_copy = k  #현재 피로도를 다른 변수에 복사
        tmp = 0     #몇 개의 던전을 돌 수 있는지 저장
        
        for need, use in i:
            if k_copy >= need:
                k_copy -= use
                tmp += 1
                
        answer = max(answer, tmp)
            
    
    return answer