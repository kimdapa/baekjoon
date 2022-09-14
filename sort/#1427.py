N = input()
a = list(map(str,N))

new_a = sorted(a, reverse = True)
sum_a = ''.join(new_a)
int_a = int(sum_a)
print(int_a)