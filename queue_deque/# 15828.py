# 15828
from collections import deque
import sys

N = int(sys.stdin.readline())
quene = deque()

while 1 :
    pakit = int(sys.stdin.readline())
    
    # pakit이 0이면 먼저 들어온 pakit 삭제
    if pakit == 0 :
        quene.popleft()
        
    # -1이 입력되면 종료
    elif pakit == -1 :
        break

    # 버퍼에 공간이 없으면 수용 불가
    elif len(quene) == N :
        continue

    # pakit append
    elif pakit != 0 :
        quene.append(pakit)

 # 라우터가 비어 있으면 empty 출력
if quene :
    print(*quene) # quene에 * 붙히면 원소 출력
else :
    print('empty') 