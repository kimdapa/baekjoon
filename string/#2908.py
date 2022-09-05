A, B = input().split()
reverse_number_A = ''
reverse_number_B = ''

for n_A in A :
    reverse_number_A = n_A + reverse_number_A
for n_B in B :
    reverse_number_B = n_B + reverse_number_B

list_1 = []
list_1.append(reverse_number_A)
list_1.append(reverse_number_B)

print(max(list_1))