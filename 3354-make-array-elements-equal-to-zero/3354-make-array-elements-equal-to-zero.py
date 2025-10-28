class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        temp = []
        for i in range(n):
            if nums[i] == 0:
                temp.append(i)
        cnt = 0        
        for i in temp:
            x = self.ct(nums, i)
            cnt += x
        return cnt        
    def ct(self, nums: List[int], i: int) -> bool:
        a = sum(nums[:i])
        b = sum(nums[i+1:])    
        if a == b:
            return 2
        elif a == b - 1 or a == b + 1:
            return 1   
        return 0 