n = int(input())

if sum(i for i in range(1, n) if n % i == 0) == n:
    print("P")
else:
    print("N")