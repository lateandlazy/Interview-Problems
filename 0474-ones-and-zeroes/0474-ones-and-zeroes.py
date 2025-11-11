class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        count = []
        for s in strs:
            z = s.count('0')
            o = s.count('1')
            count.append((z,o))
        for z, o in count:
            for i in range(m, z-1 ,-1):
                for j in range(n, o-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - z][j - o] + 1)  
        return dp[m][n]