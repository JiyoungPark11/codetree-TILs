i = input().split()
a = int(i[0])
b = int(i[1])

if a >= 90 :
    if 95 <= b <= 100 :
        print("100000")
    elif b >= 90 :
        print("50000")
    else :
        print("0")
else :
    print("0")