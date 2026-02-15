class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i, j):
            vis[i][j] = 1
            check = True
            if grid1[i][j] == 0:
                check = False
            for a, b in direc:
                nx = i + a
                ny = j + b
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if grid2[nx][ny] == 1 and vis[nx][ny] == 0:
                        if not dfs(nx, ny):
                            check = False            
            return check 
        cnt = 0                      
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and vis[i][j] == 0:
                    if dfs(i, j):
                        cnt += 1
        return cnt 