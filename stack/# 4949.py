while 1 :
    stack = []
    gwalho = list(str(input()))
    
    if len(gwalho) == 1 and "." in gwalho :
        break
    
    for i in range(len(gwalho)) :
        if gwalho[i] == '(' or gwalho[i] == '[' :
            stack.append(gwalho[i])
        elif gwalho[i] == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
        elif gwalho[i] == ']' :
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else :
                stack.append(']')

    if not stack :
        print('yes')
    else : 
        print('no')