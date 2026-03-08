class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        temp = []
        def func(s, i):
            if i == n:
                temp.append(s)
                return
            func(s + '0', i+1)
            func(s + '1', i+1) 
        s = ''    
        func(s, 0)
        for st in temp:
            if st not in nums:
                return st 


       