class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                temp = -1
                if nums[j] < nums[i]:
                    temp = dp[j] + 1
                if temp > dp[i]:
                    dp[i] = temp
        return max(dp)