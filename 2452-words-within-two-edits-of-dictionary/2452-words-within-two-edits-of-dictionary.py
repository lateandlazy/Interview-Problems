class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check(a, b):
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1
            return cnt        
        res = []
        n = len(queries)
        for nm in queries:
            for mn in dictionary:
                if check(nm, mn) <= 2:
                    res.append(nm)
                    break
        return res            