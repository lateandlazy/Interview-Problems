class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        qu = deque([])
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    qu.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1    
        if fresh == 0: return 0
        if not qu: return -1
        minutes = 0
        while qu and fresh > 0:
            minutes += 1
            for _ in range(len(qu)):
                a, b = qu.popleft()
                for x, y in direc:
                    nx = a + x
                    ny = b + y
                    if nx >= 0 and nx < n and ny >= 0 and ny < m:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh -= 1
                            qu.append((nx, ny))   
        if fresh == 0:
            return minutes
        return -1