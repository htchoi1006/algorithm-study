import math

n = int(input())
tmp = list(map(int,input().split()))
num1 = 1
for i in tmp:
    num1 *= i
    
m = int(input())
tmp = list(map(int,input().split()))
num2 = 1
for i in tmp:
    num2 *= i
    
# print(num1, num2)

print(str(math.gcd(num1, num2))[-9:])