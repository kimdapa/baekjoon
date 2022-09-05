N = int(input()) # 전체 사람의 수 N 
x = [list(map(int, input().split())) for _ in range(N)] # 각 사람의 몸무게와 키

for i in range(N) :
    point = 1 # 랭킹 저장
    for j in range(N) :
        if x[i][0] < x[j][0] and x[i][1] < x[j][1] : # 현재 덩치와 다음 번 째 덩치를 비교했을 때 더 작으면 등수가 낮아짐
            grade += 1
    print(point, end = ' ')