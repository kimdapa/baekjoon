# 1181 
N = int(input())
list1 = []

for i in range(N) :
    sentence = str(input())
    list1.append(sentence)
    
# 중복 제거 
list_n = set(list1)
list_n = list(list_n)

# sort는 문자열도 정리해줌
list_n.sort()


# 길이에 따라 sort
list_n.sort(key = len)

for i in range(len(list_n)) :
    print(list_n[i])