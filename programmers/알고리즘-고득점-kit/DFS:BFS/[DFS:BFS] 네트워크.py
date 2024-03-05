def solution(n, computers):
    answer = 0
    visited = [False] * n  #dfs가 방문했는지 확인하기 위한 리스트
    
    for i in range(n):  #각 컴퓨터리스트 돌기
        if visited[i] == False:  #만약 방문 안했으면 
            dfs(n, computers, i, visited)
            answer += 1
        
    
    return answer


def dfs(n, computers, i, visited):
    visited[i] = True
    for connect in range(n): 
        if connect != i and computers[i][connect] == 1:  #내 컴퓨터가 아닌 다른 컴퓨터와 서로 연결된 경우
            if visited[connect] == False:  #다른 컴퓨터 만약 방문 안했으면
                dfs(n, computers, connect, visited)
                
                