from itertools import permutations
import math

def check(n):  #소수인지 체크하는 함수
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    

def solution(numbers):
    num = list(numbers)  #"17" -> ['1', '7']로 리스트화 시킴
    queue = []
    answer = 0
    
    
    for i in range(1, len(num)+1):
        for j in permutations(num, i):  #가능한 순열 조합 생성
            tmp = int(''.join(j))       #('1', '7') -> 17 로 변환
            if tmp not in queue and tmp > 1:  #이 숫자가 아직 큐에 없고, 1보다 큰 수면 큐에 추가
                queue.append(tmp)
                    
                    
    while queue:
        if check(queue.pop()):  #큐에서 숫자 하나 빼서 소수인지 체크하는 함수 돌림
            answer += 1         #소수이면 answer에 1 더해줌
            
        
    
    return answer