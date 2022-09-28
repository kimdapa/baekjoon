# 9093
N = int(input())


# split word
for i in range(N) :
    sentence = list(input().split())
    complete_list = []
    
    for j in range(len(sentence)) :
        change_word = sentence[j]
        reverse_word = change_word[::-1]
        complete_list.append(reverse_word)
    print(' '.join(complete_list))