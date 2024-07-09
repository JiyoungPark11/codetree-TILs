i = input().split()
a = int(i[0])
b = int(i[1])
c = int(i[2])

if a > b and a > c :
    print(a)
elif a < b and b > c :
    print(b)
else :
    print(c)