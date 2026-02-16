class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        vis = [[-1 for _ in range(m)]for _ in range(n)]
        qu = deque([])
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    vis[i][j] = 0
                    qu.append((i,j))
        while qu:
            a, b = qu.popleft()
            for x, y in direc:
                nx = a + x 
                ny = b + y
                if nx >= 0 and nx < n and ny >= 0 and ny < m:
                    if vis[nx][ny] == -1:
                        vis[nx][ny] = vis[a][b] + 1
                        qu.append((nx, ny))
        return vis 