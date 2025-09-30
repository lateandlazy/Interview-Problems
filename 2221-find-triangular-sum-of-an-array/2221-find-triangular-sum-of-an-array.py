class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        n = len(nums)
        while n > 1:
            for i in range(n-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            nums.pop()    
            n = len(nums)    
        return nums[0] 