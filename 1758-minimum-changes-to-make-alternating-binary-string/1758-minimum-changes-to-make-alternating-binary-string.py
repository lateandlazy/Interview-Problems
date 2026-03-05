class Solution:
    def minOperations(self, s: str) -> int:
        cnt0 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    cnt0 += 1
            else:
                if s[i] != '1':
                    cnt0 += 1
        return min(cnt0, len(s) - cnt0)