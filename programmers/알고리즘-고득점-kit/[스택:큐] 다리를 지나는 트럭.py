from collections import deque


def solution(bridge_length, weight, truck):
    cnt = 0
    bridge = [0] * bridge_length
    bridge = deque(bridge)
    truck = deque(truck)
    w = 0  #현재 다리의 무게
    
    while True:
        if not truck and sum(bridge) == 0:  #남은 트럭도 없고 다리에도 트럭이 없으면
            break

        cnt += 1  #시간 초 세기
        w -= bridge.popleft()  #다리의 맨 앞에 있는 트럭 빼내기 & 현재 다리 무게에서 해당 트럭의 무게 제거
        
        
        if truck and truck[0] + w <= weight:  #새 트럭이 다리에 왔을 때 무게가 기준무게를 넘지 않으면
            t = truck.popleft() #다리의 맨 앞에 있는 트럭 제거
            bridge.append(t)    #다리에 새 트럭 올리기
            w += t              #다리 무게에 새 트럭 무게 추가
            
        else:
            bridge.append(0)    #현재 다리에 있는 트럭만 한 칸 앞으로 이동
            
    
    return cnt