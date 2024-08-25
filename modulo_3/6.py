c = int(input())

for _ in range(c):
  perros = tuple(sorted(map(int, input().split(", "))))
  f1 = 0
  f2 = 0
  max1 = 0
  min2 = -1

  for i in range(len(perros)):
    if f1 <= f2:
      f1 += perros[max1]
      max1 += 1
      continue
    f2 += perros[min2]
    min2 -= 1
  print(abs(f2-f1))
