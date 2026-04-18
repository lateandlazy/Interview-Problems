class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = str(n)[::-1]
        return abs(n - int(m))