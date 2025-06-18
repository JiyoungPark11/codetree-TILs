inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0
item_num = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        item_num += 1

avg = round(sum_val / item_num, 1)
print(sum_val, avg)