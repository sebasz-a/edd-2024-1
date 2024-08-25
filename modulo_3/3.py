from bisect import bisect_right

c = int(input())

for _ in range(c):
    p = int(input().split()[-1])
    nums = tuple(map(int, input().split(" ")))
    if nums[0] != 1 or nums[-1] != p:
        print("No es PrimiConjunto")
        continue
    
    aux = 1
    es_primi_conjunto = True
    for i in range(2, p//2 + 1):
        if p % i == 0:
            if nums[aux] != i:
                print("No es PrimiConjunto")
                es_primi_conjunto = False
                break
        if nums[aux] != i:
            aux = bisect_right(nums, i)
            continue
        aux += 1

    if es_primi_conjunto:
        print("Es PrimiConjunto")
