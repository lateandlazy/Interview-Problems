class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        k = len(needle)
        for i in range(0, n - k + 1):
            if haystack[i:i+k] == needle:
                return i
        return -1          