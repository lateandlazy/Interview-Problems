class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        MIN = float('inf')
        n = len(nums)
        if n == 1 or k == 1:return 0
        nums.sort()
        i = 0
        j = k
        while j <= n:
            mx = max(nums[i:j])
            mn = min(nums[i:j])
            diff = mx - mn
            if diff < MIN:
                MIN = diff
            i += 1
            j += 1
        return MIN