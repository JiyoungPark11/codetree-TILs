i = input().split()
a = int(i[0])
b = int(i[1])
c = int(i[2])

if a >= b :
    if a >= c :
        print(a)
    else :
        print(c)
else :
    if  b >= c :
        print(b)
    else :
        print(c)