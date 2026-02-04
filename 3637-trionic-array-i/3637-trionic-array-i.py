class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4: return False
        def inc_check(ar):
            if len(ar) == 1: return True
            for i in range(len(ar) - 1):
                if ar[i] >= ar[i+1]:
                    return False
            return True
        def dec_check(ar):
            if len(ar) == 1: return True
            for i in range(len(ar)-1):
                if ar[i] <= ar[i+1]:
                    return False
            return True                            
        for i in range(1, n - 2):
            for j in range(i+1, n-1):
                if inc_check(nums[0:i+1]) and inc_check(nums[j:n]) and dec_check(nums[i:j+1]):
                    return True
        return False            

