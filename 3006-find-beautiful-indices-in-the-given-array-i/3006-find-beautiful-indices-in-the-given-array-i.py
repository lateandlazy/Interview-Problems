class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        m = len(a)
        p = len(b)
        res = []
        ia = []
        ib = []
        if m > n or p > n:return []
        for i in range(n-m+1):
            if s[i:i+m] == a:
                ia.append(i)
        for i in range(n-p+1):
            if s[i:i+p] == b:
                ib.append(i)
        if not ia or not ib: return []
        for i in ia:
            for j in ib:
                if abs(i - j) <= k:
                    res.append(i)
                    break
        res.sort()
        return res