class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid)
        m = len(grid[0])
        y = grid[0][0] % x
        temp = []
        for i in range(n):
            for j in range(m):
                temp.append(grid[i][j])
                if grid[i][j] % x != y:
                    return -1
        temp.sort()
        idx = len(temp) // 2
        cnt = 0
        target = temp[idx]
        for num in temp:
            cnt += abs(target - num) // x
        return cnt

                 
                    
