class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        w = 0
        for i in range(n):
            if nums[i] != val:
                nums[w] = nums[i]
                w += 1
        return w  


        

