while(True):
    stack = []
    n = input()
    if(n == "0"):
        break
        
    if(len(n) == 1):
        print("yes")
    else:
        for i in n:
            stack.append(i)
        
        for j in range(len(stack)//2):
            if(stack[j] != stack[len(stack)-j-1]):
                print("no")
                break
            else:
                if(j == len(stack)//2 -1):
                    print("yes")
                else:
                    continue