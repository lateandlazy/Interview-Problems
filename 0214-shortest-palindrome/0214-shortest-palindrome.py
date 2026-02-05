class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: return ""
        if n == 1: return s
        if s == s[::-1]:
            return s
        def is_pal(ss):
            if ss == ss[::-1]:
                return True
            else:
                return False        
        for i in range(n-1, -1 ,-1):
            if is_pal(s[0:i]):
                res = s[i:][::-1] + s
                return res