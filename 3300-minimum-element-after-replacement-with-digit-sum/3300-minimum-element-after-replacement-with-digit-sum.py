class Solution:
    def minElement(self, nums: List[int]) -> int:
        def numSum(num: int):
            temp = num
            res = 0
            while temp > 0:
                res += temp % 10
                temp = temp // 10
            return res    
        mx = float('inf')
        for num in nums:
            x = numSum(num)
            if x < mx:
                mx = x
        return mx  