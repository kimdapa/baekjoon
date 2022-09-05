N,M = map(int, input().split())# N = 카드 개수, M = 딜러가 외치는 수 
A = [int(x) for x in input().split()]  # 카드에 쓰여 있는 수 

sums = [] # 세 숫자들의 합 리스트
res = 0

# 세 숫자들의 합 리스트 구하기
for i in range(0,N) : 
    for j in range(i+1,N) :
        for k in range(j+1,N) :
            y = A[i] + A[j] + A[k]
            diff = M - y 
            if diff >= 0 and M - res >= diff :
                res = y 
            y = 0

# 출력 
print(res)    