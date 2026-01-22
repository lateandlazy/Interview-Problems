class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col= len(grid[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = set()
        def bfs(r, c):
            peri = 0
            qu = deque()
            qu.append((r, c))
            vis.add((r,c)) 
            while qu:
                a, b = qu.popleft()
                for dx, dy in direc:
                    nx = dx + a
                    ny = dy + b
                    if(nx < 0 or ny < 0  or nx >= row or ny >= col or grid[nx][ny] == 0):
                        peri += 1
                    elif (nx, ny) not in vis:
                        vis.add((nx, ny))
                        qu.append((nx, ny))
            return peri
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return bfs(i, j)
        return 0  