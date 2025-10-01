class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        extra = 0
        while numBottles > 0:
            ans += numBottles
            total = numBottles + extra
            temp = (total // numExchange)
            extra = total % numExchange
            numBottles = temp    
        return ans 