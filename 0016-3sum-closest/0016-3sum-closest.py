class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target: return target
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1      
        return res