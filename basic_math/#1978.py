N = int(input())
A = [int(x) for x in input().split()]
cnt = N

for i in A :
    if i == 1 :
        cnt -= 1 
    elif i == 2 or i == 3 :
        continue
    for j in range(2, i - 1) :
        if i % j == 0 :
            cnt -= 1
            break
print(cnt)