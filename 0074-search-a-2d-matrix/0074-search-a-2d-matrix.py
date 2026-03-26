class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n = len(mat)
        m = len(mat[0])
        temp = -1
        for i in range(n):
            if mat[i][-1] >= target:
                temp = i 
                break
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