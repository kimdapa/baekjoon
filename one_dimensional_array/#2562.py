k = []
for i in range(0, 9) :
    N = int(input())
    k.append(N)
    
print(max(k))
print(k.index(max(k))+1)
