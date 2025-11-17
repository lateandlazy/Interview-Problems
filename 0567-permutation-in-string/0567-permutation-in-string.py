from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m: return False
        fq1 = defaultdict(int)
        fq2 = defaultdict(int)
        for s in s1:
            fq1[s] += 1
        for i in range(n):
            fq2[s2[i]] += 1 
        if fq1 == fq2: return True    
        i = 0
        j = n 
        while j < m:
            fq2[s2[j]] += 1
            fq2[s2[i]] -= 1
            if fq2[s2[i]] == 0: del fq2[s2[i]]
            i += 1
            j += 1
            if fq1 == fq2: return True
        return False               



                    
        