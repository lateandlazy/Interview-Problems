class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        temp = ''
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    temp += str(h)
                    temp += ":"
                    if m < 10:
                        temp += "0"
                    temp += str(m)
                    res.append(temp)
                    temp = ''
        return res 