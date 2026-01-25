class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        MIN = float('inf')
        n = len(nums)
        if n == 1:return 0
        if k >= 2:
            nums.sort()
            for i in range(n-1):
                diff = nums[i+1] - nums[i]
                if diff < MIN:
                    MIN = diff
            return MIN                       