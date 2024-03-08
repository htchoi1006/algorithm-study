from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[-1]*102 for _ in range(102)]   #
    visited = [[1]*102 for _ in range(102)]  #방문했는지 확인 + 목적지까지의 칸 수 계산
    answer = 0
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x:x*2, r)  #좌표를 모두 두배씩 해줌(ㄷ자 모양을 ㅁ으로 인식하지 않기 위함)
        for i in range(x1, x2+1):  
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:  #사각형 안에 포함되는 부분은 0으로 설정
                    arr[i][j] = 0
                elif arr[i][j] != 0:  #사각형 테두리는 1로 설정
                    arr[i][j] = 1
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((characterX*2, characterY*2)) #좌표를 두배씩 해주었기 때문에 캐릭터 좌표도 두배로 설정
    visited[characterX*2][characterY*2] == 0   #visited 배열에서 시작 위치는 0으로 설정
    
    while queue:
        x, y = queue.popleft()
        if x == itemX*2 and y == itemY*2:  #캐릭터가 아이템에 도착하면
            answer = visited[x][y] // 2    #아이템까지 걸어간 거리 / 2
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if arr[nx][ny] == 1 and visited[nx][ny] == 1:  #다음 갈 곳이 사각형 테두리이고, 아직 방문한 적이 없으면
                queue.append((nx, ny))  #큐에 추가
                visited[nx][ny] = visited[x][y] + 1  #이전 거리 + 1
        
    
    return answer



