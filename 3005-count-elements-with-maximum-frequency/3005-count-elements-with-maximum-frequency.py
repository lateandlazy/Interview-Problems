class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        fr = defaultdict(int)
        m = 0
        for num in nums:
            fr[num] += 1
            if fr[num] > m:
                m = fr[num]
        q = []        
        for i, j in fr.items():
            q.append(j)
        z = q.count(m)
        return z * m  

