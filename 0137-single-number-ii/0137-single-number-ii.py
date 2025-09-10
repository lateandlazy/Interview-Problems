class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        for num in nums:
            dp[num] += 1
        for i, j in dp.items():
            if j == 1:
                return i    