import heapq

def mix(x, y):  #스코빌 지수 섞는 함수
    return (x + y*2)

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)  #스코빌 리스트를 heap으로 만듦
    
    while len(scoville) >= 2 and scoville[0] < K:  #스코빌 리스트 원소 개수가 2개 이상이고, 제일 작은 원소가 K보다 작을 때
        mix_result = mix(heapq.heappop(scoville), heapq.heappop(scoville))  #두개 섞음
        cnt += 1  #섞은 횟수 카운트
        heapq.heappush(scoville, mix_result)  #섞은 결과를 heap에 다시 넣음
        
    if len(scoville) == 1 and scoville[0] < K:  #스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1 리턴
        return -1

        
    return cnt

