from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0]*m for _ in range(n)]  #방문했는지 체크 + 도착지까지 필요한 칸 수 세기 위함
    queue = deque()
    
    queue.append((0, 0))  #(0, 0)부터 시작
    visited[0][0] = 1     #(0, 0)은 방문했다고 체크
        
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()  #현재 있는 칸

        for i in range(4):
            nx = x + dx[i]  #행 계산
            ny = y + dy[i]  #열 계산
            
            #만약 nx, ny가 맵 밖으로 나가지 않고, 방문한 적도 없으며, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1  #이전 칸보다 한 칸 더 갔다는 뜻
                queue.append((nx, ny))  #큐에 추가

                        
    answer = visited[-1][-1]
    return answer if answer > 0 else -1   #답이 0이면 목적지까지 갈 수 없는 맵이라는 뜻 -> -1 반환