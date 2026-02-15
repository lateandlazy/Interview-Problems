class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        t = image[sr][sc]
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        image[sr][sc] = color
        vis = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i, j, direc, vis):
            image[i][j] = color 
            vis[i][j] = 1
            for a, b in direc:
                nx = i + a
                ny = j + b
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if image[nx][ny] == t and vis[nx][ny] == 0:
                        dfs(nx, ny, direc, vis)
            return            
        dfs(sr, sc, direc, vis)
        return image