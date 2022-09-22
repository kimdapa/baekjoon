N = input()

# 변경되야 되는 단어들
list_ch = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=','z=']

for i in list_ch :
    N = N.replace(i, '*')
    
print(len(N))