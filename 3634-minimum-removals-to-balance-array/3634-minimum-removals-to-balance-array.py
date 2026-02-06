class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        if n == 1: return 0
        cnt = 0
        res = 0
        for i in range(n):
            if k * nums[cnt] < nums[i]:
                cnt += 1
            curr = i - cnt + 1
            res = max(res, curr)
        return n - res        