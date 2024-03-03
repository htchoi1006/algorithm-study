from collections import deque

def solution(priorities, location):
    queue = deque(priorities)  #우선순위가 들어있는 리스트를 deque로 만듦
    loc = deque([i for i in range(len(priorities))])  #각각의 우선순위에 해당하는 인덱스도 deque로 만듦
    cnt = 0  #내가 찾는 원소가 몇번째로 나왔는지 카운트하기 위한 변수
    
    while queue:
        x = 0
        
        if queue[0] == max(queue):  #첫번째 원소의 우선순위가 가장 큰 경우
            queue.popleft()  #리스트에서 제거
            cnt += 1  
            x = loc.popleft()  #이 우선순위에 해당하는 인덱스도 제거
            
            if x == location:  #만약 이게 내가 찾는 원소일 경우 반복문 스탑
                break

        else:  #내가 찾는 원소가 아니면 우선순위 리스트와 인덱스 리스트를 모두 앞으로 한칸씩 땡김
            queue.rotate(-1)  
            loc.rotate(-1)
        
    
    return answer