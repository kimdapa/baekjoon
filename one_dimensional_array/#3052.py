N = list(int(input()) for _ in range(10))
emp = []

for i in range(10) :
    emp.append(N[i] % 42)

emp = set(emp) # 중복 제거
print(len(emp))