inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0

for i in range(a, b+1):
    if i % 2 == 0:
        sum_val += i

print(sum_val)