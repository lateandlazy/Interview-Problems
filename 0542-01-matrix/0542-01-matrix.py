class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        direc = [(0,1),(1,0),(0,-1),(-1,0)]
        qu = deque([])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    qu.append((i,j))
                else:
                    mat[i][j] = -1
        while qu:
            a, b = qu.popleft()
            for k, l in direc:
                nx = a + k
                ny = b + l
                if nx < 0 or nx == n or ny < 0 or ny == m or mat[nx][ny] != -1:
                    continue
                mat[nx][ny] = mat[a][b] + 1
                qu.append((nx, ny))
        return mat 