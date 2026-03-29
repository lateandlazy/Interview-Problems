class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        ev1 = []
        od1 = []
        ev2 = []
        od2 = []
        fq1 = defaultdict(int)
        fq2 = defaultdict(int)
        for i in range(len(s1)):
            if i % 2 == 0:
                ev1.append(s1[i])
                ev2.append(s2[i])
            else:
                od1.append(s1[i])
                od2.append(s2[i])    
            fq1[s1[i]] += 1
            fq2[s2[i]] += 1
        ev1.sort()
        ev2.sort()
        od1.sort()
        od2.sort()    
        if fq1 != fq2:
            return False
        if ev1 != ev2:
            return False
        if od1 != od2:
            return False
        return True                   