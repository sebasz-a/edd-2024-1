n = int(input())
a = tuple(input().split(", "))
out = ""

for i in range(1, n//2+1):
    out += a[i-1]
    out += a[n-i]
if n % 2 != 0:
    out += a[n//2]
print(out)
