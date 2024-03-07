from collections import deque


def solution(tickets):
    return bfs(tickets)

def bfs(tickets):
    answer = []
    queue = deque()
    queue.append(('ICN', ['ICN'], []))  #도착한 공항, 현재까지 경로, 방문한 곳의 인덱스를 저장할 리스트
    
    while queue:
        end, path, visited = queue.popleft() 
        if len(visited) == len(tickets):  #여태까지 방문한 공항의 개수와 티켓의 개수가 같으면, 즉 모든 티켓을 다 사용했으면
            answer.append(path)           #현재까지 경로를 answer에 추가
        
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == end and not idx in visited:   #출발하는 공항이 현재 도착한 공항과 일치하고, 아직 사용하지 않은 티켓이면
                queue.append((ticket[1], path+[ticket[1]], visited+[idx])) #큐에 추가
                
    answer.sort()  #answer 정렬
    
    return answer[0]  #사전순으로 앞서는 값 출력