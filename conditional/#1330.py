A,B = map(int, input().split()) # map : 입력 받은 문자를 int로 변환 시켜 줌.
if A > B : 
    print('>')
elif A < B :
    print('<')
else : 
    print('==')