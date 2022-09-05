N = input()

list1 = []
for i in N:  # Wa를 하나하나 저장
    list1.append(i)

# dial 목록
# dial_list = ['1', 'ABC', 'DEF',
             #'GHI','JKL','MNO',
             #'PQRS','TUV','WXYZ']
dial_list1 = ['A','B','C','D','E','F',
            'G','H','I','J','K','L',
            'M','N','O','P','Q','R',
            'S','T','U','V','W','X',
            'Y','Z']

# 'o'를 추가한 것 = 리스트 숫자를 맞추기 위해서
dial2_list = 'A','B','C','o'
dial3_list = 'D','E','F','o'
dial4_list = 'G','H','I','o'
dial5_list = 'J','K','L','o'
dial6_list = 'M','N','O','o'
dial7_list = 'P','Q','R','S'
dial8_list = 'T','U','V','o'
dial9_list = 'W','X','Y','Z'

# dial_list와 겹치는 알파벳 저장 리스트
list_new = []

# 겹치는 알파벳 찾기
for dial in dial_list1 : 
    for alpha in list1 :
        if dial == alpha : 
            list_new.append(dial)

# 시간 계산기            
result = 0

for n in range(len(list_new)) :
    for j in range(4) :
        if dial2_list[j] == list_new[n] :
            result += 3
        elif dial3_list[j] == list_new[n] :
            result += 4
        elif dial4_list[j] == list_new[n] :
            result += 5 
        elif dial5_list[j] == list_new[n] :
            result += 6
        elif dial6_list[j] == list_new[n] :
            result += 7
        elif dial7_list[j] == list_new[n] :
            result += 8
        elif dial8_list[j] == list_new[n] :
            result += 9
        elif dial9_list[j] == list_new[n] :
            result += 10 

print(result)