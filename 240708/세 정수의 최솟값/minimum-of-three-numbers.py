i = input().split()
a = int(i[0])
b = int(i[1])
c = int(i[2])

if a <= b and a <= c :
    print(a)
elif b <= a and b <= c :
    print(b)
elif c <= a and c <= b :
    print(c)