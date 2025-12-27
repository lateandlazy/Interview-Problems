class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr = sum(nums[0:k])
        res = curr
        i = 0
        j = k - 1
        while j < n-1:
            j += 1
            curr += nums[j]
            curr -= nums[i]
            i += 1
            if res < curr:
                res = curr
        return res / k 