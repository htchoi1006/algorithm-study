import heapq

def solution(jobs): 
    ans = 0 
    start, end = -1, 0 
    heap = [] 
    cnt = len(jobs) 
    
    while cnt:   #jobs 개수 만큼 반복문
        for time, work in jobs:  
            if start < time <= end:    #이미 작업이 실행중이면 heap에 넣기
                heapq.heappush(heap, [work, time])  #작업이 요청되는 시점과 작업 소요 시간을 뒤집어서 넣기 (정렬 위함)

        if len(heap) > 0:  #heap에 작업이 들어있으면
            x, y = heapq.heappop(heap)   #x : 작업 소요 시간 , y : 작업이 요청되는 시점
            start = end  #원래 끝 시간 -> 현재 시작 시간으로 변경
            end += x   #끝 시간 + 작업 소요시간
            ans += (end - y)  #총 소요 시간 += (끝 시간 - 작업이 요청되는 시점)
            cnt -= 1
            
        else:
            end += 1  
    
    return int(ans/len(jobs))