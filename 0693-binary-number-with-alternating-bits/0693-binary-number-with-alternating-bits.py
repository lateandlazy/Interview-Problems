class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        st = bin(n)[2:]
        for i in range(1,len(st)):
            if st[i] == st[i-1]:
                return False
        return True        
