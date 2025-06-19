cnt = 0

while cnt <= 3:
    cnt += 1
    n = int(input())
    if n % 2 == 1:
        continue
    else:
        print(n // 2)
    