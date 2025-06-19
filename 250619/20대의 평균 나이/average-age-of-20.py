sum_val = 0
cnt = 0

while True:
    n = int(input())

    if n >= 30:
        break
    
    cnt += 1
    sum_val += n

avg = round(sum_val/cnt, 2)
print(f"{avg:.2f}")