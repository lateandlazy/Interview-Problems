class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        WALL, GUARD, GUARDED = 1, 2, -1
        gd = [[0 for _ in range(n)] for _ in range(m)]
        for i, j in walls:
            gd[i][j] = WALL
        for i, j in guards:
            gd[i][j] = GUARD     
        for i, j in guards:
            for x in range(i + 1, m):
                if gd[x][j] == 0:
                    gd[x][j] = GUARDED
                elif gd[x][j] in (WALL, GUARD):
                    break
            for x in range(i - 1, -1, -1):
                if gd[x][j] == 0:
                    gd[x][j] = GUARDED
                elif gd[x][j] in (WALL, GUARD):
                    break 
            for y in range(j + 1, n):
                if gd[i][y] == 0:
                    gd[i][y] = GUARDED
                elif gd[i][y] in (WALL, GUARD):
                    break 
            for y in range(j - 1, -1, -1):
                if gd[i][y] == 0:
                    gd[i][y] = GUARDED
                elif gd[i][y] in (WALL, GUARD):
                    break               
        count = sum(gd[i][j] == 0 for i in range(m) for j in range(n))
        return count     