# 2751
N = int(input())
list1 = []

for _ in range(N) :
    list1.append(int(input()))
    
def quick(list1) :
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(list1) <= 1 :
        return list1
    
    pivot = list1[0] # 피벗은 첫 번째 원소
    tail = list1[1:] # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick(left_side) + [pivot] + quick(right_side)

for i in range(len(list1)) :
    print(quick(list1)[i])