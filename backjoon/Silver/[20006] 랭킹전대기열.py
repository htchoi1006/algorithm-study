n, m = map(int, input().split())
rooms = []

for _ in range(n):
    level, name = input().split()
    
    if not rooms:
        rooms.append([[int(level), name]])
        continue
        
    enter = False
    
    for room in rooms:
        if len(room) < m and abs(room[0][0] - int(level)) <= 10:
            room.append([int(level), name])
            enter = True
            break
    
    if not enter:
        rooms.append([[int(level), name]])
        
        
for room in rooms:
    room.sort(key=lambda x:x[1])
    
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for level, name in room:
        print(level, name)
        
        

        
    
    