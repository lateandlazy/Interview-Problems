class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        ans = ''
        temp = ''
        for i in range(n):
            if s[i] == ' ':
                if not temp: continue
                ans = temp + ' ' + ans
                ans += ' '
                temp = ''
            else:
                temp += s[i]
        ans = temp + ' ' + ans
        return ans.strip()               



        