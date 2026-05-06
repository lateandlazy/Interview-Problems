class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])     
        res = [['.'] * n for _ in range(m)]
        for i in range(n):
            cnt = 0
            for j in range(m):
                if boxGrid[i][j] == '#':
                    cnt += 1
                elif boxGrid[i][j] == '*':
                    res[j][n-i-1] = '*'
                    if cnt > 0:
                        k = j - 1
                        while cnt > 0:
                            res[k][n-i-1] = '#'
                            cnt -= 1
                            k -= 1
                        cnt = 0    
            if cnt > 0:
                k = m - 1
                while cnt > 0:
                    res[k][n-i-1] = '#'
                    cnt -= 1
                    k -= 1
        return res         

                