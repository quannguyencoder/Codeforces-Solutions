def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    cnt += nums[0] % 2 == 0
    cnt += nums[1] % 2 == 0
    cnt += nums[2] % 2 == 0
    even = True
    if cnt < 2:
        even = False
    for i, num in enumerate(nums):
        if even and num % 2 != 0:
            return i + 1
        elif not even and num % 2 == 0:
            return i + 1
 
print(solve())