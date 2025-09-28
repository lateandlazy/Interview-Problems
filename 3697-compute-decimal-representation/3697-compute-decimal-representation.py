class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        ans = []
        power = 1
        while n > 0:
            d = n % 10
            if d > 0:
                temp = d * power
                ans.append(temp)
            n = n // 10
            power = power * 10
        return ans[::-1]    
                
                