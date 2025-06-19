n = int(input())
cnt = 0

for i in range(1, n+1):
    # print("i = ", i)
    # print("n = ", n)
    n //= i      
    # print("div = ", div)
    cnt += 1  
    if n <= 1:
        break

print(cnt)
    