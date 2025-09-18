class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        ans = ''
        temp = ''
        for i in range(n):
            if int(num[i]) % 2 != 0:
                temp += num[i]
                ans = temp
            else:
                temp += num[i]
        return ans 