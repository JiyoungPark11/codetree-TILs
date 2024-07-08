i = input().split()
a = int(i[0])
b = int(i[1])

if a >= 90 :
    if 95 <= b < 100 :
        print("10")
    elif b >= 90 :
        print("5")
    else :
        print("0")
else :
    print("0")