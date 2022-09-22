N = [1,1,2,2,2,8]
W = list(map(int, input().split()))

for i in range(len(N)) :
    k = N[i] - W[i]
    print(k)