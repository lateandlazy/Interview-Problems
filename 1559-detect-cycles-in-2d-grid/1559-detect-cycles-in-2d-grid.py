class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _ in range(n)]
        direc  = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(x,y,xp,yp):
            vis[x][y] = 1
            for a, b in direc:
                nx = x + a
                ny = y + b
                if n > nx >= 0 and m > ny >= 0 and grid[nx][ny] == grid[x][y]:
                        if vis[nx][ny] == 1:
                            if nx != xp or ny != yp:
                                return True
                        else:
                            if dfs(nx,ny,x,y):
                                return True
            return False            
        for i in range(n):
            for j in range(m):
                if vis[i][j] == 0:
                    if dfs(i,j,-1,-1):
                        return True

        return False


