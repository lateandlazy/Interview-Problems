class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid > x // mid:
                high = mid - 1
            elif mid < x // mid:
                low = mid + 1
            else:
                return mid
        return high    