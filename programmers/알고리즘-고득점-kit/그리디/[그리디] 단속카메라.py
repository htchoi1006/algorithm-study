def solution(routes):
    routes.sort(key=lambda x : x[0])  #진입 지점을 기준으로 sort
    
    camera = routes[0][1]  #첫번째 카메라는 첫번째 원소의 진출지점
    ans = 1  #카메라 개수
    
    for i, o in routes:
        if i > camera:  #진입 지점이 현재 카메라보다 크면
            camera = o  #카메라 위치를 해당 경로의 진출지점으로 변경
            ans += 1    #카메라 한 대 추가
        
        camera = min(camera, o)   #현재 카메라 위치와 진출지점 중 더 작은 값으로 카메라 위치 변경
    
    return ans