class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def can_remove(r1, c1, r2, c2, i ,j):
            rows = r2 - r1 + 1
            cols = c2 - c1 + 1
            if rows * cols == 1:
                return False
            if rows == 1:
                return j == c1 or j == c2
            if cols == 1:
                return i == r1 or i == r2
            return True 

        n = len(grid)
        m = len(grid[0])
        rPre = [0] * n
        cPre = [0] * m
        mp = defaultdict(list)

        for i in range(n):
            s = 0
            for j in range(m):
                val = grid[i][j]
                s += val
                mp[val].append((i,j))
            rPre[i] = s + (rPre[i-1] if i > 0 else 0)

        for j in range(m):
            s = 0
            for i in range(n):
                s += grid[i][j]
            cPre[j] = s + (cPre[j-1] if j > 0 else 0)

        total = rPre[-1]

        for i in range(n-1):
            top = rPre[i]
            bottom = total - top
            if top == bottom:
                return True
            diff = abs(top - bottom)
            if diff in mp:
                if top > bottom:
                    for x, y in mp[diff]:
                        if x <= i and can_remove(0,0,i,m-1,x,y):
                            return True
                else:
                    for x, y in mp[diff]:
                        if x > i and can_remove(i+1,0,n-1,m-1,x,y):
                            return True

        for j in range(m-1):
            left = cPre[j]
            right = total - left
            if left == right:
                return True
            diff = abs(left - right) 
            if diff in mp:
                if left > right:
                    for x, y in mp[diff]:
                        if y <= j and can_remove(0,0,n-1,j,x,y):
                            return True
                else:
                    for x, y in mp[diff]:
                        if y > j and can_remove(0,j+1,n-1,m-1,x,y):
                            return True
        return False