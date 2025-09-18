class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        ans = num
        for i in range(n - 1, -1,-1):
            if int(num[i]) % 2 != 0:
                return ans
            else: ans = ans[:-1]
        return ans 