a, b, c = map(int, input().split())

if a == b == c :
    print(10000 + a * 1000)
elif a == b or b == c or a == c : 
    if a == b or a == c:
        print(1000 + a * 100)
    else :
        print(1000 + c * 100)
else :
    if a > b > c or a > c > b :
        print(100 * a)
    elif b > a > c or b > c > a :
        print(100 * b)
    else :
        print(100 * c)