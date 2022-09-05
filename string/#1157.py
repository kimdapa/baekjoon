word = input().lower()
word_list = list(set(word)) # 자료형의 중복 제거 

list_1 = []

for i in word_list : # 중복 삭제
    count = word.count(i)
    list_1.append(count)

if list_1.count(max(list_1)) >= 2 :
    print('?')
else : 
    print(word_list[(list_1.index(max(list_1)))].upper())