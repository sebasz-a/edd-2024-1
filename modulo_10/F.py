def primes(n):
    aux = [True for x in range(n+2)]
    i = 2
    while i*i <= n:
        if aux[i] == True:
            for j in range(i*i, n+1, i):
                aux[j] = False
        i += 1
    out = set()
    for k in range(2, n):
        if aux[k]:
            out.add(k)
    return out

C = int(input())
pairs = {} #parejas de cada número

for _ in range(C):
    N = int(input())
    pairs[N] = set()
    c_primes = primes(N)

    count = 0
    for num in c_primes:
        if N-num in c_primes:
            pair = frozenset((num, N-num))
            if pair not in pairs[N]:
                pairs[N].add(pair)
                count += 1
    print(count)
