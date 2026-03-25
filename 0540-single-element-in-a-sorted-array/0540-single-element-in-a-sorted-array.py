class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        fq = defaultdict(int)
        for num in nums:
            fq[num] += 1
        for a, b in fq.items():
            if b == 1:
                return a 