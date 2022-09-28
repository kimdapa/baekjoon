# 10828
N = int(input())
stack_list = []

for i in range(N) :
    order = input().split()
    
    if order[0] == 'push' :
        stack_list.append(order[1])
    
    elif order[0] == 'pop' :
        if len(stack_list) == 0 :
            print(-1)
        else :
            print(stack_list.pop()) # pop() = last delete
    
    elif order[0] == 'size' :
        print(len(stack_list))
    
    elif order[0] == 'empty' :
        if len(stack_list) == 0 :
            print(1)
        else :
            print(0)
    
    elif order[0] == 'top' :
        if len(stack_list) == 0 :
            print(-1)
        else :
            print(stack_list[-1])