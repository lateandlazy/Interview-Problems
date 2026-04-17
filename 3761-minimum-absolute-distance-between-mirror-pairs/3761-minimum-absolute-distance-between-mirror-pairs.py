class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 10 ** 9
        fq = defaultdict(int)
        for i in range(n):
            if nums[i] in fq:
                res = min(res, i - fq[nums[i]])
            fq[int(str(nums[i])[::-1])] = i
        return res if res != 10 ** 9 else -1    