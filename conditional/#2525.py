A, B = map(int, input().split())
C = int(input())

if B + C < 60 :
    B = B + C
else : 
    k = int((B + C) / 60)
    A += k
    if A >= 24 :
        A -= 24 
    B = (B + C) % 60 
    
print(A, B)