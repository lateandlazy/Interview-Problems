class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ar = []
        count = 1
        for i in range(n):
            if i == n - 1:
                ar.append(count)
            elif s[i] == s[i+1]:
                count += 1
            else:
                ar.append(count)
                count = 1       
        res = 0        
        for j in range(len(ar)-1):
            res += min(ar[j], ar[j+1])
        return res              