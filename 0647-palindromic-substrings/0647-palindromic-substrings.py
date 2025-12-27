class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1: return 1
        count = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count