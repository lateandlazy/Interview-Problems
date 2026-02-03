class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        if k == 1:return nums
        cnt = 0
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                cnt += 1
            else:
                cnt = 0
            if i >= k - 1:
                if cnt >= k - 1:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res                
