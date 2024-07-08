x = input().split()
a = int(x[0])
b = x[1]

y = input().split()
c = int(y[0])
d = y[1]

if a >= 19 or c >= 19 :
    if b == 'M' or d == 'M' :
        print("1")
    else :
        print("0")
else :
    print("0")