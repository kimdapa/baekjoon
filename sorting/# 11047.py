# 11047
N, K = input().split()
c_list = []
coin_gatsu = 0

N = int(N)
K = int(K)


# 동전 종류
for i in range(N) :
    coin = int(input())
    c_list.append(coin)

c_list.sort(reverse = True)
    
for i in range(N) :
    coin_gatsu += K // c_list[i]
    K = K % c_list[i]
    
print(coin_gatsu)