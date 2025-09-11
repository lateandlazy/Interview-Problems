class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        res = -1
        for a in arr:
            freq[a] += 1
        for num, count in freq.items():
            if num == count:
                if num > res:
                    res = num
        return res            