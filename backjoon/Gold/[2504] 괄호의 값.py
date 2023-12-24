stack = list(input())
# stack = ['(', '(', ')', '[', '[', ']', ']', ')', '(', '[', ']', ')']
# print(stack)
tmp = []
res = 1
result = 0

for i in range(len(stack)):
    if stack[i] == '(':
        res *= 2
        tmp.append(stack[i])
    elif stack[i] == '[':
        res *= 3
        tmp.append(stack[i])
    elif stack[i] == ')':
        if not tmp or tmp[-1] != '(':
            result = 0
            break
        if stack[i-1] == '(':
            result += res
        res //=2
        tmp.pop()
    elif stack[i] == ']':
        if not tmp or tmp[-1] != '[':
            result = 0
            break
        if stack[i-1] == '[':
            result += res
        res //= 3
        tmp.pop()
        
if tmp:
    print(0)
else:
    print(result)
