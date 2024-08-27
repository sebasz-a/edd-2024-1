pdd = set()
pdi = set()
pdc = set()

while True:
    inp = tuple(input().split())
    votante = inp [0]
    if votante == "#":
        print(len(pdd - pdi - pdc | pdi - pdd - pdc | pdc - pdi - pdd), end=" ")
        print(len(pdd & pdi - pdc | pdd & pdc - pdi | pdi & pdc - pdd), end=" ")
        print(len(pdd & pdi & pdc))
        break
    partido = inp[1]
    if partido == "pdd":
        pdd.add(votante)
    elif partido == "pdi":
        pdi.add(votante)
    else:
        pdc.add(votante)
