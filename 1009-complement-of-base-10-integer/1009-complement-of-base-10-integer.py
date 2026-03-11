class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = bin(n)[2:]
        temp = ''
        for ch in x:
            if ch == '0':
                temp += '1'
            else:
                temp += '0'
        return int(temp, 2)            
