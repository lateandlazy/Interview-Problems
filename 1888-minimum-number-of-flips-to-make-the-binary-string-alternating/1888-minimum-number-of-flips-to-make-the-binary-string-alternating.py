class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        ans1, ans2 = 0, 0
        res = float('inf')
        for i in range(len(s)):
            if s[i] != ('0' if i % 2 == 0 else '1'):
                ans1 += 1
            if s[i] != ('1' if i % 2 == 0 else '0'):
                ans2 += 1
            if i >= n:
                if s[i - n] != ('0' if (i - n) % 2 == 0 else '1'):
                    ans1 -= 1
                if s[i - n] != ('1' if (i - n) % 2 == 0 else '0'):
                    ans2 -= 1
            if i >= n - 1:
                res = min(res, ans1, ans2)    
        return res