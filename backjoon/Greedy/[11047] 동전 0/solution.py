n, money = map(int, input().split())
coin = []
for i in range(n):
    tmp = int(input())
    coin.append(tmp)

coin = sorted(coin, reverse=True)

count = 0

for i in coin:
    if(i <= money):
        count += money//i
        money = money%i
        if(money <= 0):
            break
        
        
print(count)