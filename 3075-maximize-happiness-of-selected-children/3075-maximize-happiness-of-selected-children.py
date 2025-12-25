class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort()
        i = n - 1
        j = 0
        s = 0
        while k > 0:
            x = happiness[i] - j
            if x <= 0:
                break
            else:    
                s += x
            k -= 1
            j += 1
            i -= 1
        return s    
