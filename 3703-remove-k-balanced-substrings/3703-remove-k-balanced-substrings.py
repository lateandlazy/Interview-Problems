class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        temp = ''
        for i in range(k):
            temp += '('
        for i in range(k):
            temp += ')'
        while temp in s:
            s = s.replace(temp,"")
        return s        
