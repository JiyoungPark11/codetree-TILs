i = input().split()
a = i[0]
b = i[1]
c = i[2]

if a > b and a > c :
    print(a)
elif b > a and b > c :
    print(b)
else :
    print(c)