n = int(input())

for i in range(n):
    for _ in range(n-i):
        print("*", end='')
    for _ in range(2*i):
        print(" ", end='')
    for _ in range(n-i):
        print("*", end='')
    print()