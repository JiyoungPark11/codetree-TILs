while True:
    inp = input()
    arr = inp.split()
    h = int(arr[0])
    w = int(arr[1])
    c = arr[2]

    print(h*w)
    
    if c == 'C':
        break
    else:
        continue
    