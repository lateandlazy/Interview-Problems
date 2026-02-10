class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(0, n):
            fqO = defaultdict(int)
            fqE = defaultdict(int)
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    fqE[nums[j]] += 1
                else:
                    fqO[nums[j]] += 1
                if len(fqE) == len(fqO):
                    res = max(res, j - i + 1) 
        return res 