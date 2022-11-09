# 11399
N = int(input())
P = list(map(int, input().split())) 
sum_time = 0

# 시간 리스트

P.sort()

for i in range(N) :
    sum_time += P[i] * (N - i)
    
print(sum_time)