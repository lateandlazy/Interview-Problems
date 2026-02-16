class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i, j):
            vis[i][j] = 1
            for a, b in direc:
                nx = i + a 
                ny = j + b
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if vis[nx][ny] == 0 and grid[nx][ny] == 0:
                        dfs(nx, ny)     
        for i in range(n):
            for j in [0,m-1]:
                if grid[i][j] == 0 and vis[i][j] == 0:
                    dfs(i, j)
        for j in range(m):
            for i in [0, n-1]:
                if grid[i][j] == 0 and vis[i][j] == 0:
                    dfs(i, j)
        cnt = 0            
        for i in range(1,n-1):
            for j in range(1, m-1):
                if grid[i][j] == 0 and vis[i][j] == 0:
                    dfs(i, j)
                    cnt += 1    
        return cnt                                