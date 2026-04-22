class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def check(a, b):
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1
                    if cnt > 2:
                        return False
            return True       
        res = []
        n = len(queries)
        for nm in queries:
            for mn in dictionary:
                x = check(nm, mn)
                if x:
                    res.append(nm)
                    break
        return res            