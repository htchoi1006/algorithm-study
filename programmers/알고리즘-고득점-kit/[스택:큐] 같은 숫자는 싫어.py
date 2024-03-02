def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1, len(arr)):  
        if arr[i] == arr[i-1]:  #앞의 수와 중복되면 패스
            continue
        else:  #앞의 수와 다르면 배열에 추가
            answer.append(arr[i])
                    
    
    return answer