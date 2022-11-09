# 11651
N = int(input())
list1 = []

for i in range(N) :
    x = input().split()
    list1.append((int(x[0]), int(x[1])))
    
list_s = sorted(list1, key = lambda x : (x[1], x[0]))

for i in range(len(list_s)) :
    print(list_s[i][0], list_s[i][1])