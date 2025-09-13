class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ar = defaultdict(int)
        ar[5], ar[10], ar[20] = 0, 0, 0
        for bill in bills:
            if bill == 5:
                ar[5] += 1
            elif bill == 10:
                if ar[5] > 0:
                    ar[5] -= 1
                    ar[10] += 1
                else:
                    return False
            elif bill == 20:
                if ar[5] > 0 and ar[10] > 0:
                    ar[5] -= 1
                    ar[10] -= 1
                    ar[20] += 1
                elif ar[5] >= 3:
                    ar[20] += 1
                    ar[5] -= 3    
                else:
                    return False
        return True