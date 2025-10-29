class Solution:
    def smallestNumber(self, n: int) -> int:
        x = bin(n)
        n = len(x) - 2
        z = '1' * n
        return int(z, 2)