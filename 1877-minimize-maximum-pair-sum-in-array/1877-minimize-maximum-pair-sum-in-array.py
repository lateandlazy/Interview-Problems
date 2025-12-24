class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        r = n - 1
        res = -1
        while l < r:
            x = nums[l] + nums[r]
            res = max(res, x)
            l += 1
            r -= 1
        return res    