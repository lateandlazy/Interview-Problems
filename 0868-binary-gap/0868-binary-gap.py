class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        res = -1
        index = -1
        for i in range(len(b)):
            if b[i] == '1':
                if index ==  -1:
                    index = i
                else:
                    res = max(res, i-index)
                    index = i  
            else:
                continue
        if res == -1:
            return 0
        return res                  