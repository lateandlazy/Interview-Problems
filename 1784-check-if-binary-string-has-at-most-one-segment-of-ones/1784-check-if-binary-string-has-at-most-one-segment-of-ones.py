class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        if n == 1 and s == '1':return True
        for i in range(1,n):
            if s[i] == '1' and s[i-1] == '0':
                return False
        return True 