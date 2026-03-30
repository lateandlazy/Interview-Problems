class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        ev1 = []
        ev2 = []
        od1 = []
        od2 = []
        for i in range(0,n,2):
            ev1.append(s1[i])
            ev2.append(s2[i])
        for i in range(1,n,2):
            od1.append(s1[i])
            od2.append(s2[i]) 
        ev1.sort()
        ev2.sort() 
        od1.sort()
        od2.sort()
        if ev1 != ev2:
            return False
        if od1 != od2:
            return False
        return True              
