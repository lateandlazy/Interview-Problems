class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        vis1 = [[0 for _ in range(m)] for _ in range(n)]
        vis2 = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i ,j, vis):
            vis[i][j] = 1
            for a, b in direc:
                nx = i + a
                ny = j + b
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if heights[nx][ny] >= heights[i][j] and vis[nx][ny] == 0:
                        dfs(nx, ny, vis)                       
        for i in range(n):
            if vis1[i][0] == 0:
                dfs(i, 0, vis1)
        for j in range(1, m):
            if vis1[0][j] == 0:
                dfs(0, j, vis1)
        for i in range(n):
            if vis2[i][m-1] == 0:
                dfs(i, m-1, vis2)
        for j in range(m):
            if vis2[n-1][j] == 0:
                dfs(n-1, j, vis2) 
        res = [] 
        for i in range(n):
            for j in range(m):
                if vis1[i][j] == 1 and vis2[i][j] == 1:
                    res.append((i, j))
        return res