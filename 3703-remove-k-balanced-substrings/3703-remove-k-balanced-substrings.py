class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        temp1 = ''
        temp2 = ''
        for i in range(k):
            temp1 += '('
            temp2 += ')'
        temp = temp1 + temp2    
        while temp in s:
            s = s.replace(temp,"")
        return s        
