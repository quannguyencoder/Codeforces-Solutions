from collections import Counter
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    seen = Counter(nums)
    unique_nums = sorted(list(set(nums)))
    cur_n = len(unique_nums)
    dp = [0] * (cur_n + 2)
    for i in range(cur_n - 1, -1, -1):
        cur = unique_nums[i]
        total = seen[cur] * cur
        
        if i + 1 < cur_n and unique_nums[i + 1] - cur == 1:
            next_idx = i + 2
        else:
            next_idx = i + 1
        skip = dp[i + 1]
        choose = total + dp[next_idx]
        dp[i] = max(choose, skip)
    return dp[0]
    # @cache
    # def dp(i):
    #     if i >= len(unique_nums):
    #         return 0
    #     cur = unique_nums[i]
    #     total = seen[cur] * cur
    #     if i == len(unique_nums) - 1:
    #         return total 
    #     skip = dp(i + 1)
    #     if unique_nums[i + 1] - cur != 1:
    #         next_idx = i + 1 
    #     else:
    #         next_idx = i + 2
    #     choose = total + dp(next_idx)
        
    #     return max(skip, choose)
    # return dp(0)
print(solve())