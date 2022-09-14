# 2108
import math
import sys
from collections import Counter

N = int(sys.stdin.readline())
n = []
for _ in range(N):
    n.append(int(sys.stdin.readline()))
    
n.sort()


# 산술평균
sum_n = sum(n) / N 
sansul = round(sum_n, 0)
print(math.floor(sansul))

# 중앙값
middle_n = sorted(n, reverse = False)
print(middle_n[math.floor(N/2)]) 

# 최빈값
n.sort()
count = Counter(n).most_common(2)

if len(n) > 1:
    if count[0][1] == count[1][1] :
        print(count[1][0])
    else :
        print(count[0][0])
else:
    print(count[0][0])

# 범위
print(max(n) - min(n))