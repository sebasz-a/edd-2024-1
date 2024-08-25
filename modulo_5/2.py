C = int(input())

for _ in range(C):
    N, K = map(int, input().split())
    estudiantes = [x for x in range(1, N + 1)]
    K -= 1

    while True:
        sale = estudiantes.pop(K)
        N -= 1
        pasos = sale % N
        if pasos == 0:
            pasos = 1
        K = ((K + pasos) % N) - 1
        if K == -1:
            K = N - 1
        if N == 1:
            print(estudiantes.pop())
            break
