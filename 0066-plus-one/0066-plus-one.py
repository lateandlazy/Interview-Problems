class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        while True:
            if i < 0:
                digits = [1] + digits
                break
            if digits[i] + 1 > 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] = digits[i] + 1
                break
        return digits  
