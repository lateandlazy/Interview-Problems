class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bias = n * (99 // n) + n
        res = []
        for i in range(n):
            res.append(nums[(i + nums[i] + bias) % n])
        return res 