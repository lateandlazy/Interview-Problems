class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        fqs = defaultdict(int)
        fqp = defaultdict(int)
        for i in range(m):
            fqs[s[i]] += 1
        for i in range(m):
            fqp[p[i]] += 1
        if fqs == fqp:
            res.append(0)
        for i in range(1,n-m+1):
            fqs[s[i-1]] -= 1
            fqs[s[i+m-1]] += 1
            if fqs == fqp:
                res.append(i)
        return res

        
        