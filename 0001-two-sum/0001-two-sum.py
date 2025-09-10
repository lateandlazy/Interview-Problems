class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = []
        left = 0
        for i in range(n):
            for j in range(i + 1, n) :
                if nums[i] + nums[j] == target:
                    res = [i] + [j]
        return res            
                    

            