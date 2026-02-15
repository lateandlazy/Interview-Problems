class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i, j, vis, direc):
            vis[i][j] = 1
            if grid[i][j] == 1:
                grid[i][j] = 2
                for a, b in direc:
                    nx = i + a
                    ny = j + b
                    if nx >= 0 and ny >= 0 and nx < n and ny < m:
                        dfs(nx, ny, vis, direc)
            else: return            
        jth = [0, m-1]  
        ith = [0, n-1]                    
        for i in range(n):
                for j in jth:
                    if vis[i][j] == 0 and grid[i][j] == 1:
                        dfs(i, j, vis, direc)
        for j in range(1, m - 1):
                for i in ith:
                    if vis[i][j] == 0 and grid[i][j] == 1:
                        dfs(i, j, vis, direc)                
        cnt = 0            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
        return cnt                                            