# 18258
import sys
from collections import deque

N = int(sys.stdin.readline())
quene = deque()

for _ in range(N) :
    order = sys.stdin.readline().split()
    
    if order[0] == 'push' :
        quene.append(order[1])
    
    elif order[0] == 'pop' :
        if len(quene) == 0 :
            print(-1)
        else :
            print(quene[0]) # pop() = last delete
            quene.popleft()
            
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