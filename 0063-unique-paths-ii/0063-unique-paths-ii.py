class Solution:
    def uniquePathsWithObstacles(self, Grid: List[List[int]]) -> int:
        r = len(Grid)
        c = len(Grid[0])
        if Grid[-1][-1] == 1 or Grid[0][0] == 1:return 0
        mat = [[0 for _ in range(c)]for _ in range(r)]
        mat[0][0] = 1
        for i in range(1,c):
            if Grid[0][i] == 0 and mat[0][i-1] == 1:
                mat[0][i] = 1
        for i in range(1,r):
            if Grid[i][0] == 0 and mat[i-1][0] == 1:
                mat[i][0] = 1
        for i in range(1, r):
            for j in range(1, c):
                if Grid[i][j] == 1:
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]    
        return mat[r-1][c-1] 