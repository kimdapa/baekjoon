# 9012
T = int(input())

for i in range(T) :
    stack = []
    gwalho = list(str(input()))
    for j in range(len(gwalho)) :
        if gwalho[j] == '(' :
            stack.append(gwalho[j])
        elif gwalho[j] == ')' :
            if stack :
                stack.pop()
            else :
                print('NO')
                break
    else : 
        if not stack :
            print('YES')
        else : 
            print('NO')