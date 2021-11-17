def solution(prices):
    second = [0]*len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if(prices[i] <= prices[j]):
                second[i] += 1
            else:
                second[i] += 1
                break
            
    return second