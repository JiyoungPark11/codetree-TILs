sum_val = 0
item = 0

for _ in range(10):
    n = int(input())
    if 0 <= n <= 200:
        sum_val += n
        item += 1
    
avg = round(sum_val / item, 1)
print(sum_val, avg)
