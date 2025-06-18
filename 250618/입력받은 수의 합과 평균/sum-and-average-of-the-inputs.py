n = int(input())
sum_val = 0

for _ in range(n):
    m = int(input())
    sum_val += m

avg = round(sum_val / n, 1)
 
print(sum_val, avg)