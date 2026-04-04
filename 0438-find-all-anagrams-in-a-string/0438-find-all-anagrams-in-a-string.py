from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        #ss = Counter(s[0:m])
        pp = Counter(p)
        for i in range(0,n-m+1):
            if Counter(s[i:m+i]) == pp:
                res.append(i)
        return res
        