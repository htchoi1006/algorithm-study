n = int(input())

for _ in range(n):
    string = list(input())
    length = len(string)
    i, j = 0, 1
    
    for idx in range(1, length):
        if string[idx] > string[idx-1]:
            if i < idx:
                i = idx
                
    for idx in range(1, length):
        if string[idx] > string[i-1]:
            if j < idx:
                j = idx
                
    if i != 0 and j != 0:
        string[i-1], string[j] = string[j], string[i-1]
        string[i:] = list(reversed(string[i:]))
        
    print(''.join(string))