class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        w = 0
        count = 0
        for i in range(0,n):
            if s[i] == '0':
                count += (i - w)
                w += 1
        return count 