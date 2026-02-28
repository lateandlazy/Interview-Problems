class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9+7
        s=''
        i = 1
        while i <= n:
            temp = bin(i)[2:]
            s += temp
            i += 1
        res = int(s, 2)
        return res % mod    