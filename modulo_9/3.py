ejer1 = set()
N1 = int(input())
for _ in range(N1):
    ejer1.add(input())

ejer2 = set()
N2 = int(input())
for _ in range(N2):
    ejer2.add(input())

ejer3 = set()
N3 = int(input())
for _ in range(N3):
    ejer3.add(input())

ejer4 = set()
N4 = int(input())
for _ in range(N4):
    ejer4.add(input())

ejer5 = set()
N5 = int(input())
for _ in range(N5):
    ejer5.add(input())

ganadores = ejer1.intersection(ejer2, ejer3, ejer4, ejer5)
if not ganadores:
    print("Nadie gana")
else:
    print(1000000 // len(ganadores))
