class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        for ch in t:
            if i < n and s[i] == ch:
                i += 1
        if i == n:
            return True
        return False