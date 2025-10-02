class Solution:
    def maxBottlesDrunk(self, numB: int, numE: int) -> int:
        ans = numB
        empty = numB
        while empty >= numE:
            ans += 1
            empty -= numE - 1
            numE += 1      
        return ans    
