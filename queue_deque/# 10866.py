# 10866
import sys
from collections import deque

N = int(sys.stdin.readline())
quene = deque()

for _ in range(N) :
    order = sys.stdin.readline().split()
    
    if order[0] == 'push_front' :
        quene.appendleft(order[1])
    
    elif order[0] == 'push_back' :
        quene.append(order[1])
    
    elif order[0] == 'pop_front' :
        if len(quene) == 0 :
            print(-1)
        else :
            print(quene.popleft()) # pop() = last delete
            
            
    elif order[0] == 'pop_back' :
        if len(quene) == 0 :
            print(-1)
        else :
            print(quene.pop())
            
    elif order[0] == 'size' :
        print(len(quene))
    
    elif order[0] == 'empty' :
        if len(quene) == 0 :
            print(1)
        else :
            print(0)
    
    elif order[0] == 'front' :
        if len(quene) == 0 :
            print(-1)
        else :
            print(quene[0])
            
    elif order[0] == 'back' :
        if len(quene) == 0 :
            print(-1)
        else :
            print(quene[-1])