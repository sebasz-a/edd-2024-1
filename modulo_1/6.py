n  = int(input())

while n != 1:
    print(n)
    if n % 2 == 0:
        n //= 2
        continue
    n = 3*n + 1
print(n)