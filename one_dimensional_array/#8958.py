N = int(input())

for i in range(N) :
    quiz = list(input())
    count = 0 
    sum_q = 0
    for quiz_ox in quiz :
        if quiz_ox == 'O' :
            count += 1
            sum_q += count
        else :
            count = 0 
    print(sum_q)