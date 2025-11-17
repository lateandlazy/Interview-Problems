class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        t = -1
        for i in range(n):
            if nums[i] == 1:
                if t == -1:
                    t = i
                else:
                    if i - t - 1 < k:
                        return False
                    t = i
        return True                    