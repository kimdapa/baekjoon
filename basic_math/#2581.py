M = int(input())
N = int(input())
num = list(range(M, N+1))

for i in range(M, N+1) : 
    if i != 1 : 
        for j in range(2, i-1) :
            if i % j == 0 :  
                num.remove(i)
                break
    elif i == 1 :
        num.remove(i)

if not len(num) :
    print(-1)
else :
    print(sum(num))
    print(min(num))