class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fq = defaultdict(int)
        for num in nums:
            fq[num] += 1
            if fq[num] > 1:
                return num