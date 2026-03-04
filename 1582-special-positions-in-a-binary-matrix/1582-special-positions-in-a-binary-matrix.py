class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ro = defaultdict(int)
        co = defaultdict(int)
        n = len(mat)
        m = len(mat[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    ro[i] += 1
                    co[j] += 1
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if ro[i] == 1 and co[j] == 1:
                        count += 1
        return count  