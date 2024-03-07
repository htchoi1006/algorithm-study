from collections import deque

def solution(answers):
    student1 = deque([1, 2, 3, 4, 5])  #1번 학생 찍기 방식
    student2 = deque([2, 1, 2, 3, 2, 4, 2, 5])  #2번 학생 찍기 방식
    student3 = deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])  #3번 학생 찍기 방식
    solve = [0, 0, 0]  #각자 몇문제 풀었는지 저장하는 리스트
    
    for i in answers:
        if i == student1[0]:
            solve[0] += 1
        if i == student2[0]:
            solve[1] += 1
        if i == student3[0]:
            solve[2] += 1
        
        #한 문제 채점했으면 다음 문제로 돌려줌
        student1.rotate(-1) 
        student2.rotate(-1)
        student3.rotate(-1)
    
    
    answer = []
    for i in range(3): #문제를 제일 많이 맞힌 학생을 리스트에 저장
        if solve[i] == max(solve):
            answer.append(i+1)
            
    
    return answer


