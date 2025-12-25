class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        res = []
        temp = ''
        for i in range(n):
            if i == n - 1:
                temp += s[i]
                a = self.rev(temp)
                res.append(a)
                break
            elif s[i] == ' ':
                a = self.rev(temp)
                res.append(a)
                temp = ''
            else:
                temp += s[i]  
        return " ".join(res)              
    def rev(self, t:str) -> str:
        l = list(t)
        n = len(l)
        i = 0
        j = n - 1
        while i < j :
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        return "".join(l) 