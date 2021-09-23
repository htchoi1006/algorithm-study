import sys

str = sys.stdin.readline()

a = list(str)
answer = ""

i = 0
start = 0

while(i < len(a)):
    if(a[i] == "<"):
        i += 1
        while(a[i] != ">"):
            i += 1
        i += 1
        
    elif(a[i].isalnum() == True):
        start = i
        while(i < len(a) and a[i].isalnum()):
            i += 1
        tmp = a[start:i]
        tmp.reverse()
        a[start:i] = tmp

        
    else:
        i += 1
        
        
print("".join(a))