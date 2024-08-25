import heapq
     
A, pa = [], 0
B, pb = [], 0
C, pc = [], 0
 
while True:
    entrada = input()
 
    if entrada == "fin del juego":
        print(f"Equipo A: {pa}\nEquipo B: {pb}\nEquipo C: {pc}")
        break
 
    if entrada == "menores":
        la, lb, lc = len(A), len(B), len(C)
        if la == lb == lc == 0:
            continue
        
        ganadores = ""
        if la > 0:
            ganadores += "A"
        if lb > 0:
            if not ganadores:
                ganadores += "B"
            elif B[0] < A[0]:
                ganadores = "B"
                heapq.heappop(A)
            elif B[0] == A[0]:
                ganadores += "B"
            else: heapq.heappop(B)
        if lc > 0:
            if not ganadores:
                ganadores += "C"
            elif ganadores[0] == "A":
                if C[0] < A[0]:
                    ganadores = "C"
                    heapq.heappop(A)
                elif C[0] == A[0]:
                    ganadores += "C"
                else: heapq.heappop(C)
            elif ganadores[0] == "B":
                if C[0] < B[0]:
                    ganadores = "C"
                    heapq.heappop(B)
                elif C[0] == B[0]:
                    ganadores += "C"
                else: heapq.heappop(C)
        
        for ganador in ganadores:
            if ganador == "A":
                pa += 1
                heapq.heappop(A)
                continue
            if ganador == "B":
                pb += 1
                heapq.heappop(B)
                continue
            pc += 1
            heapq.heappop(C)
        continue
 
    equipo, numero = entrada.split()
    if equipo == "A":
        heapq.heappush(A, int(numero))
        continue
    elif equipo == "B":
        heapq.heappush(B, int(numero))
        continue
    else:
        heapq.heappush(C, int(numero))
