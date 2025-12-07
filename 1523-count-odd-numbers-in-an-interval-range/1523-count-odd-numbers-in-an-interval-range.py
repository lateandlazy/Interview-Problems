import math
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high == 0:return 0
        s = high - low
        d = s / 2
        if high % 2 == 0 and low % 2 == 0:
            return int(d)
        elif high % 2 != 0 and low % 2 != 0:
            return int(d) + 1
        else:
            return math.ceil(d)