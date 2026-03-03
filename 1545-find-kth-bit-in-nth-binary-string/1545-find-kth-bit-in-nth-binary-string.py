class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverse(x):
            return x[::-1]
        def invert(x):
            temp = ''
            for ch in x:
                if ch == '0':
                    temp += '1'
                else:
                    temp += '0'
            return temp            
        s = '0'
        m = n
        while m > 1:
            ss = reverse(invert(s))
            temp = s + '1' + ss
            s = temp
            m -= 1
        return s[k-1] 
