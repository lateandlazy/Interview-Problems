class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        ar = []
        for i in range(n):
            if nums[i] == 1:
                ar.append(i)
        if not ar: return True
        if len(ar) == 1 : return True        
        m = len(ar)   
        for i in range(m-1):
            if ar[i+1] - ar[i] - 1 < k: 
                return False
        return True        


