def solution(numbers):
    numbers = list(map(str, numbers))
    # numbers.sort(key=lambda x: x.ljust(4, '0'), reverse=True)  --> 4번케이스 통과못함
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)   #34의 경우 34343434로 만든 다음 앞 4자리만 비교에 사용
    
    
    answer = int(''.join(numbers))  #000 -> 0 으로 만들기 위함
    return str(answer)