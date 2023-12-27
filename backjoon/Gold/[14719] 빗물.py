n, m = map(int, input().split())
city = list(map(int, input().split()))
water = 0

for i in range(1, m-1):
    leftmax = max(city[:i])
    rightmax = max(city[i+1:])
    
    compare = min(leftmax, rightmax)
    
    if city[i] < compare:
        water += compare - city[i]

print(water)