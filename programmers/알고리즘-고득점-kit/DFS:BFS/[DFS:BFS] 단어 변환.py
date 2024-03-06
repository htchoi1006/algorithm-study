from collections import deque

def bfs(begin, target, words):
    queue = deque()
    queue.append((begin, 0))  #시작 단어와 횟수를 큐에 추가
    
    while queue:
        now, cnt = queue.popleft() 
        if now == target:   #현재 단어가 찾는 단어라면 횟수 리턴
            return cnt
        
        for word in words:  #현재 단어와 알파벳 한 개만 차이나는지 체크
            tmp = 0
            for i in range(len(word)):
                if now[i] != word[i]:  
                    tmp += 1
                    
            if tmp == 1:  #현재 단어와 알파벳 한 개만 차이난다면 큐에 추가
                queue.append((word, cnt+1))
                
                
    

def solution(begin, target, words):
    if target not in words:  #찾는 단어가 단어 리스트에 없으면 0 리턴
        return 0
                        
    return bfs(begin, target, words)




