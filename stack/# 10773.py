# 10773 
K = int(input())
list1 = []

# 0 들어오면 전의 원소 삭제, 아니면 리스트에 추가
for i in range(K) :
    x = int(input())
    if x == 0 :
        list1.pop()
    else :
        list1.append(x)

# list1 비어 있으면 0 출력, 아니면 list1 출력 
if not list1 :
    print('0')
else :
    print(sum(list1))