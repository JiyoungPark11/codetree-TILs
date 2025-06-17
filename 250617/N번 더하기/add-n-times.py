inp = input()
arr = inp.split()
a = int(arr[0])
n = int(arr[1])

b = a + n
print(b)
for _ in range(n-1):
    b += n
    print(b)
