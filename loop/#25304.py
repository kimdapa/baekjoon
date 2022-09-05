X = int(input()) # 물건의 총 금액
N = int(input()) # 물건의 종류 수
money = int(0)

for i in range(1, N+1) :
    a,b = map(int, input().split())
    ans = a * b
    money += ans    

if X == money :
    print("Yes")
else : 
    print("No")