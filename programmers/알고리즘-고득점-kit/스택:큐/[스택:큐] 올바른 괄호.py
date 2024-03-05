def solution(s):
    answer = True
    arr = []
    
    for i in s:
        if i == '(':  #여는 괄호가 나오면 스택에 추가
            arr.append(i)
        elif i == ')' and len(arr) > 0: #닫는 괄호가 나오고 스택에 여는 괄호가 들어있으면 
            arr.pop()
        elif i == ')' and len(arr) == 0: #닫는 괄호가 나오고 스택이 비어있으면
            answer = False
            break
    
    if arr: #for문이 끝났는데도 스택에 괄호가 남아있으면
        answer = False
                
            

    return answer