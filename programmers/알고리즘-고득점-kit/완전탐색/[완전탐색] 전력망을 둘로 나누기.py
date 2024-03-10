from collections import deque

def solution(n, wires):
    answer = 0
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:  #각 송전탑마다 연결된 송전탑 저장
        graph[a].append(b)
        graph[b].append(a)
        
    print(graph)
        
        
    def bfs(start):  #연결된 송전탑 개수 카운트하는 함수
        visited = [0] * (n+1)
        queue = deque([start])
        visited[start] = 1
        cnt = 1
        
        
        while queue:  #연결된 송전탑 타고 타고 들어가기
            s = queue.popleft()
            for i in graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
                    cnt += 1
                    
        return cnt
    
    
    answer = n
    for a, b in wires:
        graph[a].remove(b)  #송전탑 전선 끊기
        graph[b].remove(a)  #송전탑 전선 끊기
        
        answer = min(abs(bfs(a) - bfs(b)) , answer)
        
        graph[a].append(b)  #전선 끊은 송전탑 다시 연결
        graph[b].append(a)  #전선 끊은 송전탑 다시 연결
        
    
    return answer





