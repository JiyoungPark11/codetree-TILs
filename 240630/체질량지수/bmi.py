data = input().split()
h = int(data[0])
w = int(data[1])

bmi = 10000 * w // (h * h)
print(bmi)

if bmi >= 25 :
    print("Obesity")