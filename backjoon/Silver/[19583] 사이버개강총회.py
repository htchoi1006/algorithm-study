import sys
input = sys.stdin.readline

start, middle, end = input().split()
start = int(start[:2] + start[3:])
middle = int(middle[:2] + middle[3:])
end = int(end[:2] + end[3:])

attend = set()
cnt = 0

while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= start:
            attend.add(name)
        elif middle <= time <= end and name in attend:
            attend.remove(name)
            cnt += 1
            
    except:
        break
        
print(cnt)
