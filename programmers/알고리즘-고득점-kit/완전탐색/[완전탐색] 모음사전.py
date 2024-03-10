from itertools import product

def solution(word):
    arr = []
    vowel = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6): #한글자부터 여섯글자까지
        for j in product(vowel, rep eat=i):  #중복순열로 가능한 모든 조합 만듦
            arr.append(''.join(j)) 
            
    arr.sort()  
    
    return arr.index(word)+1