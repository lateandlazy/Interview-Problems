class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        j = 2*k - 1
        while j <= n-1:
            if self.check(nums[i:i+k]) and self.check(nums[i+k:j+1]):
                return True
            i += 1
            j += 1
        return False        
    def check(self,ar: List[int]) -> bool:
        n = len(ar)
        for i in range(1,n):
            if ar[i] <= ar[i-1]:
                return False
        return True            