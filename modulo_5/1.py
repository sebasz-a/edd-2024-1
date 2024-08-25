nums = []

while True:
    inp = input().split()
    if inp[0] == "E":
        break
    t, n = inp
    if t == "A":
        nums.append(int(n))
        continue
    if t == "M":
        out = 0
        for num in nums:
            if num % int(n) == 0:
                out += num
        print(out)
