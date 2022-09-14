N,k = map(int, input().split()) # 응시자의 수, 상을 받는 사람의 수 
x = [int(i) for i in input().split()] # 각 학생의 점수 

winner = [] # empty list

new_x = sorted(x, reverse = True)

print(new_x[k-1])