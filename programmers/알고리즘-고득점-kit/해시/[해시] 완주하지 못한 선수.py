def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:  #둘이 다르면 리턴
            return participant[i]
    
    return participant[-1]  #앞이 다 똑같은 경우 맨 뒤에 있는 선수가 못들어왔으므로 리턴
        