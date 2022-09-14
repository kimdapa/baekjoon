N = int(input()) # input

n = list(int(input()) for _ in range(N)) # numbers input

new_n = sorted(n, reverse = False) # sort

for i in range(len(new_n)): 
    print(new_n[i])