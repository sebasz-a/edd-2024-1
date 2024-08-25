from bisect import bisect

int(input())
nums = tuple(map(int, input().split(" ")))
int(input())
c = tuple(map(int, input().split(" ")))
out = 0

for num in c:
    indx =  bisect(nums, num)
    if nums[indx-1] != num:
        continue
    out += indx
print(out)
