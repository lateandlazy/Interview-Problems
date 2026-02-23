class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        x = 2 ** k
        dd = set()
        i = 0
        j = k
        while j <= n:
            if s[i:j] not in dd:
                dd.add(s[i:j])
            i += 1
            j += 1
        if len(dd) == x:
            return True
        return False 