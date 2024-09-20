events = {}

N, Q = tuple(map(int, input().split()))
series = tuple(map(int, input().split()))

for e in series:
    if not e in events:
        events[e] = 0
    events[e] += 1

for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] not in events:
        print("NO")
    else:
        if query[1] <= events[query[0]]:
            print("SI")
        else:
            print("NO")
