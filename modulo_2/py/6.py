c = int(input())

for _ in range(c):
    n = int(input())
    board = tuple(map(int, input().split()))
    aux = 0
    out = 0

    while True:
        if (aux < 0 or aux >= n) or board[aux] == 0:
            print(out)
            break

        x = aux
        aux += board[aux]
        if x == 0:
            board = (0,) + board[1:]
        elif x == n-1:
            board = board[:n-1] + (0,)
        else:
            board = board[:x] + (0,) + board[x+1:]

        out += 1
