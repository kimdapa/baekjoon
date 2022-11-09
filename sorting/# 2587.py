# 2587 
list1 = []

for _ in range(5) :
    list1.append(int(input()))
    
list1.sort()
mean_1 = int(sum(list1) / 5)
median_1 = int(list1[2])

print(mean_1)
print(median_1)