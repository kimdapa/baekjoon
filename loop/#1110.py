N = int(input())
K = list(str(N))

old_N = N # 변수 저장
count = 1

for i in range(100) :
    if len(K) == 2 :
        T = int(K[0]) + int(K[1]) # 2 + 6 = 8 => 첫 째자리 + 둘 째 자리
        if T > 9 :
            New_T = list(str(T))
            U = int(K[1] + New_T[1])
            if U == old_N :
                print(count)
                break
            else :
                count += 1
                K = list(str(U))
        elif T < 10 :    
            U = int(K[1] + str(T)) # 6 + 8 = 14
            if U == old_N :
                print(count)
                break
            else :
                count += 1
                K = list(str(U))
    elif len(K) == 1 :
        T = int(K[0]) # 2 + 6 = 8 => 첫 째자리 + 둘 째 자리
        U = int(K[0] + str(T)) # 6 + 8 = 14
        if U == old_N :
            print(count)
            break
        else :
            count += 1
            K = list(str(U))