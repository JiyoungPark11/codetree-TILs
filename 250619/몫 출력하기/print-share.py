cnt = 0

while cnt < 4:
    cnt += 1
    n = int(input())
    if n % 2 == 1:
        continue
    if n % 2 == 0:
        print(n // 2)
    