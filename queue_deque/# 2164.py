# 2164
from collections import deque

N = int(input())
quene = deque()

# 1부터 N까지 
for i in range(N) :
    quene.append(i+1)
    
    
for i in range(N) :
    # quene에 원소가 한 개면 바로 출력
    if len(quene) == 1 :
        print(quene[0])
        break
    
    # 아닐 시 진행
    quene.popleft()
    quene.append(quene[0])
    quene.popleft()
    
    # 마지막에 남은 원소 출력
    if len(quene) == 1 :
        print(quene[0])
        break