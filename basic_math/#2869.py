# 달팽이는 올라가고 싶다

# A = 미터
# B = 미끄러지는 미터
# V = V미터의 나무
import math
A, B, V = map(int, input().split())

# A - B = 하루 올라가는 길이
# V - (A - B) = 다음 날 남은 나무 길이
# 반복문은 너무 오래 걸림
'''for i in range(0, V) :
    V = V - (A - B)
    if V < 0 :
        print(i + 1)
        break
    elif V == 0 :
        print(i)
        break'''

print(math.ceil((V - A)/ (A -B)) + 1)