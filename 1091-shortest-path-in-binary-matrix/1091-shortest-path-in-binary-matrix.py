class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        if n == 1:
            return 1    
        direc = [(1,1),(0,1),(1,0),(1,-1),(-1,1),(0,-1),(-1,0),(-1,-1)]
        qu = deque([])
        qu.append((0,0,1))
        while qu:
            a, b, d =  qu.popleft()
            for x, y in direc:
                nx = a + x
                ny = b + y
                if nx >= 0 and ny >= 0 and nx < n and ny < n:
                    if nx == n - 1 and ny == n - 1:
                        return d + 1
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        qu.append((nx,ny,d+1))
        return -1 