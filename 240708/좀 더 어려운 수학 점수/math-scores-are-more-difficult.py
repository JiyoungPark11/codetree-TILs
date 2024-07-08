x = input().split()
a = int(x[0])
b = int(x[1])

y = input().split()
c = int(y[0])
d = int(y[1])

if a > c :
    print("A")
elif a == c :
    if b > d :
        print("A")
    else :
        print("B")
else :
    print("B")