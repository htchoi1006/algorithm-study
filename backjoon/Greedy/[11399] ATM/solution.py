n = int(input())
time = list(map(int, input().split()))

time = sorted(time)

sum_time = 0

for i in range(n):
    for j in range(i+1):
        sum_time += time[j]
        
print(sum_time)