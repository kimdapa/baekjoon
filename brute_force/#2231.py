N = int(input())

# 분해합
def decomp(s) : 
    k = list(str(s)) # 자연수를 문자열로 저장 후 리스트화
    list_1 = [] # 각각을 저장할 리스트
    list_1.append(s) # N 먼저 저장
    # 각각 자리마다 리스트에 저장
    for i in range(len(str(s))) :
        list_1.append(int(k[i]))
    # T = 분해합   
    T = sum(list_1)
    return(T)

# 생성자 리스트
list_2 = []

# 생성자
for i in range(N) :
    if decomp(N-i) == N :
        list_2.append(N-i)

# 생성자가 없는 경우 0 출력 / 있는 경우 가장 작은 생성자 출력
if not list_2 :
    print(0)
else :
    print(min(list_2))