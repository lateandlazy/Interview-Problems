class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        rw = []
        cl = []
        for i in range(n):
            temp = sum(grid[i])
            rw.append(temp)
        for i in range(m):
            s = 0
            for j in range(n):
                s += grid[j][i] 
            cl.append(s)
        rSum = sum(rw)
        cSum = sum(cl)
        rPre = [0] * len(rw)
        rPre[0] = rw[0]
        cPre = [0] * len(cl)
        cPre[0] = cl[0]
        for i in range(1, len(rw)):
            rPre[i] = rPre[i-1] + rw[i]
        for i in range(1, len(cl)):
            cPre[i] = cPre[i-1] + cl[i]
        for j in range(len(rPre)-1):
            if rPre[j] == rSum - rPre[j]:
                return True
        for j in range(len(cPre)-1):
            if cPre[j] == cSum - cPre[j]:
                return True
        return False 