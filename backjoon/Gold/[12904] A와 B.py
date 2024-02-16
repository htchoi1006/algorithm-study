s = list(input())
t = list(input())

while 1:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]
    
    if s == t:
        print(1)
        break
        
    if len(t) == 0:
        print(0)
        break


    
