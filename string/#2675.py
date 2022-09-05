T = int(input()) # 테스트 개수 입력 

for i in range(T) :  # R과 S 입력을 위한 for 구문
    R,S = input().split()
    S = list(S)     
    len_S = len(S)
    for j in range(len_S) : # R 만큼 출력을 위한 for 구문
        print(S[j] * int(R), end = '')
    print()