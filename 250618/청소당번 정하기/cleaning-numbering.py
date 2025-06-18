n = int(input())
cls = 0
hall = 0
toilet = 0

for i in range(1, n+1):
    if i % 12 == 0:
        toilet += 1
    elif i % 3 == 0:
        hall += 1
    elif i % 2 == 0:
        cls += 1

print(cls, hall, toilet)