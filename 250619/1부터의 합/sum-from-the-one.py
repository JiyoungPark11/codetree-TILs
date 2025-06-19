n = int(input())
sum_val = 0

for i in range(1, 101):
    if sum_val >= n:
        print(n)
        break
    sum_val += i
