class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        while len(nums) > 1:
            temp = []
            for i in range(len(nums)-1):
                x = (nums[i] + nums[i+1]) % 10
                temp.append(x)
            nums = temp
        return nums[0] 