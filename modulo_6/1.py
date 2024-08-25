import heapq

citas = []

while True:
    turno = input()

    if turno == "sig":
        if len(citas) == 0:
            continue
        last = heapq.heappop(citas)
        continue
    if turno == "end":
        print(last)
        break
    heapq.heappush(citas, int(turno))
