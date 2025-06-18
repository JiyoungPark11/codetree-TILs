inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
sum_val = 0

if a > b:
    a, b = b, a
else: 
    pass

for i in range(a, b+1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)