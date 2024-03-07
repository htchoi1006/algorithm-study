def solution(sizes):
    width = []
    height = []
    
    for card in sizes:
        width.append(max(card))  #가로, 세로 중 큰 수는 width에 추가
        height.append(min(card)) #가로, 세로 중 작은 수는 height에 추가
    
    return max(width) * max(height) #가로의 최대값 * 세로의 최댓값