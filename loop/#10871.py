N, X = map(int,input().split())
A = [int(x) for x in input().split()] 

for i in A :
    if X > i :
        print(i)
    else :
        continue