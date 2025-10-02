class Solution:
    def maxBottlesDrunk(self, numB: int, numE: int) -> int:
        ans = 0
        empty = 0
        while numB > 0:
            ans += numB
            empty += numB
            numB = 0
            while empty >= numE:
                empty -= numE
                numB += 1
                numE += 1
        return ans        
