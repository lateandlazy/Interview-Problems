class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        grid = []
        n = len(mat)
        m = len(mat[0])
        k = k % m
        def rShift(ar):
            temp1 = ar[0:m-k]
            temp2 = ar[m-k:]
            for num in temp1:
                temp2.append(num)
            return temp2    
        def lShift(ar):
            temp1 = ar[0:k]
            temp2 = ar[k:]
            for num in temp1:
                temp2.append(num)
            return temp2    
        for i in range(n):
            if i % 2 == 0:
                grid.append(lShift(mat[i]))
            else:
                grid.append(rShift(mat[i]))    
        return grid == mat