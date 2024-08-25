n = int(input())

if n % 2 == 0:
    print("es multiplo de 2")
elif n % 3 == 0:
    print("es multiplo de 3")
elif n % 5 == 0:
    print("es multiplo de 5")
elif n % 7 == 0:
    print("es multiplo de 7")
else:
    print("no es multiplo de ninguno de los primeros cuatro primos")