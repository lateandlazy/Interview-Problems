class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        ans = []
        res = ''
        temp = ''
        for i in range(n):
            if s[i] == ' ':
                if not temp: continue
                ans.append(temp)
                temp = ''
            else:
                temp += s[i]
        ans.append(temp)        
        for x in reversed(ans):
            res = res + ' ' + x
        return res.strip()    



        