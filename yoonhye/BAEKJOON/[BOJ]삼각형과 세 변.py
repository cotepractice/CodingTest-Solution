res = []

while(1):
    a, b, c = map(int, input().split())
    total = a+b+c
    if total == 0:
        break
    if max(a,b,c) >= (total - max(a,b,c)):
        res.append("Invalid")
        continue

    if a == b == c:
        res.append("Equilateral")
    elif a!=b and b!=c and c!=a:    #세 변의 길이가 모두 다름
        res.append("Scalene")
    else:
        res.append("Isosceles")

for r in res:
    print(r)