class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        a = start.count('L')
        b = start.count('R')
        c = target.count('L')
        d = target.count('R')
        if a != c or b != d: return False
        i, j = 0, 0
        while i < n and j < n:
            while i < n and start[i] == '_': i += 1
            while j < n and target[j] == '_': j += 1
            if i < n and j < n:
                if start[i] != target[j]:
                    return False
                if i < j and start[i] == 'L':
                    return False    
                if i > j and start[i] == 'R':
                    return False
            i += 1
            j += 1
        return True  