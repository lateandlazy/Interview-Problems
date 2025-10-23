class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = ''
            for i in range(len(s)-1):
                x = (int(s[i])+int(s[i+1])) % 10
                temp += str(x)
            s = temp
        if s[0] == s[1]:
            return True
        return False            