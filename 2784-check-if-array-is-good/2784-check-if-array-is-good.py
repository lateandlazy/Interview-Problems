class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        if mx != len(nums) - 1:
            return False
        fqTable = [0] * mx     
        for num in nums:
            fqTable[num-1] += 1
        if fqTable[mx-1] != 2:
            return False
        for i in fqTable:
            if i == 0:
                return False
        return True                       

        