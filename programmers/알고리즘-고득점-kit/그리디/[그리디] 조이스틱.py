def solution(name):
    ans = 0
    move = len(name) - 1
    
    for i, letter in enumerate(name):
        ans += min(ord(letter) - 65, 91 - ord(letter))  #원하는 알파벳 찾기 (A에서 움직인 값과 Z에서 움직인 값 비교)
            
        next = i + 1  
        
        #연속되는 A 찾기
        while next < len(name) and name[next] == 'A':  #다음 알파벳이 A일 때
            next += 1
        
        #기본 움직임 값 / 왼쪽으로 움직이는 값 / 오른쪽으로 움직이는 값 비교
        move = min([move, i*2+len(name)-next, i+2*(len(name)-next)])
        # print([move, i*2+len(name)-next, i+2*(len(name)-next)])
        
    ans += move
        
    
    return ans