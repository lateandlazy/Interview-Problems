class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        fqe1 = defaultdict(int)
        fqe2 = defaultdict(int)
        fqo1 = defaultdict(int)
        fqo2 = defaultdict(int)
        for i in range(0,n,2):
            fqe1[s1[i]] += 1
            fqe2[s2[i]] += 1
        for i in range(1,n,2):
            fqo1[s1[i]] += 1
            fqo2[s2[i]] += 1
        if fqe1 != fqe2:
            return False
        if fqo1 != fqo2:
            return False
        return True              
