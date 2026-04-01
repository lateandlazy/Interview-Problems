class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], direc: str) -> List[int]:
        n = len(positions)
        lt = []
        for i in range(n):
            lt.append([positions[i],healths[i],direc[i],i])
        lt.sort()
        nw = []
        nw.append(lt[0])    
        for i in range(1,n):
            curr = lt[i]
            while nw and nw[-1][2] == 'R' and curr[2] == 'L':
                if nw[-1][1] > curr[1]:
                    nw[-1][1] -= 1
                    curr = None
                    break
                elif nw[-1][1] < curr[1]:
                    curr[1] -= 1
                    nw.pop()
                else:
                    nw.pop()
                    curr = None
                    break
            if curr:
                nw.append(curr)            
        ans = []
        nw.sort(key=lambda x: x[3])
        for a,b,c,d in nw:
            ans.append(b)
        return ans   




              

