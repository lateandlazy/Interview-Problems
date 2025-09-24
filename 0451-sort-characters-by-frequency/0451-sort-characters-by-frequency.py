class Solution:
    def frequencySort(self, s: str) -> str:
        fq = defaultdict(int)
        for a in s:
            fq[a] += 1
        fq1 = sorted(fq.items(), key =lambda item: item[1], reverse=True)    
        fq1 = dict(fq1)
        ans = ''
        for a, b in fq1.items():
            ans += a*b
        return ans  