class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        fr = defaultdict(int)
        for num in nums:
            fr[num] += 1
            if fr[num] > 2:
                return False
        return True        


