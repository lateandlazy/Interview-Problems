class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i ,j):
            vis[i][j] = 1
            count = 1
            for a, b in direc:
                nx = i + a
                ny = j + b
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if grid[nx][ny] == 1 and vis[nx][ny] == 0:
                        count += dfs(nx, ny)
            return count            
        res = 0
        temp = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    temp = dfs(i, j)
                res = max(res, temp)        
        return res   