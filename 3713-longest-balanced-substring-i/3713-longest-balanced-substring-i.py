class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        res = 0
        fq = defaultdict(int)
        def check(fq):
            c = -1
            for j in fq.values():
                if c == -1:
                    c = j
                else:
                    if j != c:
                        return False
            return True        
        for i in range(0, n-1):
            fq[s[i]] += 1
            for j in range(i+1, n):
                fq[s[j]] += 1
                if check(fq):
                    res = max(res, j - i + 1)
            fq.clear()
        return res 