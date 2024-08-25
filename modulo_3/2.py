from bisect import bisect

c = int(input())
for _ in range(c):
    nums = tuple(sorted(tuple(map(int, input().split(" ")))))
    current = nums[0] # valor actual que se esta buscando
    out = ""
    aux = 0 # variable para saber desde que indice se empieza de nuevo
    while True:
        indx = bisect(nums, current)
        if nums[-1] == current:
            out += str(indx - aux)
            break
        out += str(indx - aux) + " "
        current, aux = nums[indx], indx
    print(out)
