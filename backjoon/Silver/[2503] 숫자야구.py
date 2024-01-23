from itertools import permutations
num = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))
# print(num)

n = int(input())
# n = 4

for _ in range(n):
    guess, s, b = map(int, input().split())
    guess = list(str(guess))
    removed = 0
    
    for i in range(len(num)):
        strike, ball = 0, 0
        
        i -= removed
        for j in range(3):
            guess[j] = int(guess[j])
            if guess[j] in num[i]:
                if j == num[i].index(guess[j]):
                    strike += 1
                else:
                    ball += 1
        
        if strike != s or ball != b:
            num.remove(num[i])
            removed += 1
            
print(len(num))