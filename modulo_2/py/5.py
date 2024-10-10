c = int(input())

for _ in range(c):
    M, N = map(int, input().split())
    money = tuple(map(int, input().split()))

    totals = tuple(0 for x in range(M))

    for i in range(N):
        aux = i % M
        if aux == 0:
           totals = (totals[0] + money[i],) + totals[1:]
        elif aux == M-1:
            totals = totals[:M-1] + (totals[M-1] + money[i],)
        else:
            totals = totals[:aux] + (totals[aux] + money[i],) + totals[aux+1:]

    print(max(totals) - min(totals))
