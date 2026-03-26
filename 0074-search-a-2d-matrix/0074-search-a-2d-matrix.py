class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        temp = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if mat[mid][-1] < target:
                low = mid + 1
            elif mat[mid][-1] > target:
                high = mid - 1
            else:
                return True
        temp = high + 1    
        if temp >= n:
            return False        
        low = 0
        high = m - 1
        while low <= high:
            mid = low + (high - low) // 2
            if mat[temp][mid] < target:
                low = mid + 1
            elif mat[temp][mid] > target:
                high = mid - 1
            else:
                return True
        return False 