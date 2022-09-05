C = int(input())

for i in range(C) : 
    s_list = [int(x) for x in input().split()] # 학생 성적 입력
    del s_list[0] # 첫 번째 오는 학생 수 삭제
    s_sum = sum(s_list)
    mean = s_sum / len(s_list)  # 리스트의 평균
    
    count = 0 # 비율을 구하기 위해 변수 설정
    for student in s_list :
        if student > mean : 
            count += 1 
        else : 
            continue
    percent = count / len(s_list) * 100
    print(format(percent,".3f")+'%')