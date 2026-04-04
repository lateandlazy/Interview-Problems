class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        if n < m:return []
        res = []
        fqs = defaultdict(int)
        fqp = defaultdict(int)
        for i in range(m):
            fqs[s[i]] += 1
        for i in range(m):
            fqp[p[i]] += 1
        if fqs == fqp:
            res.append(0)    
        for i in range(m,n):
            fqs[s[i]] += 1
            fqs[s[i-m]] -= 1
            if fqs[s[i-m]] == 0:
                del fqs[s[i-m]]
            if fqs == fqp:
                res.append(i-m+1)
        return res

        
        