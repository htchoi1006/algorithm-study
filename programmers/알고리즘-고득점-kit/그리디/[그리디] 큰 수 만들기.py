def solution(number, k):
    stack = []
    
    for i in number:
        
        #스택이 비어있지 않고 맨 위의 숫자보다 i가 크고, k가 0보다 크면
        while stack and stack[-1] < i and k > 0:  
            k -= 1 
            stack.pop()  #스택 맨 위 원소 제거
        stack.append(i)  #스택에 i 추가
        
    if k != 0:  #아직 k개의 수를 다 안뺐으면 
        stack = stack[:-k]  #맨 위에 있는 원소를 제외한 나머지만 유지
        
    return ''.join(stack)