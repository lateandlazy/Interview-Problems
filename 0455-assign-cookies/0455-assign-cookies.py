class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        a, b = 0, 0
        while a < n and b < m:
            if g[a] <= s[b]:
                count += 1
                a += 1
                b += 1
            else:
                b += 1
        return count