class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        fq_s = defaultdict(int)
        fq_t = defaultdict(int)
        if m != n: return False
        for i in range(n):
            fq_s[s[i]] += 1
            fq_t[t[i]] += 1
        return fq_s == fq_t
