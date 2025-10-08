class Solution:
    def successfulPairs(self, sp: List[int], po: List[int], su: int) -> List[int]:
        po.sort()
        ans = []
        m = len(po)
        for s in sp:
            low = 0
            high = m - 1
            temp = m
            while low <= high:
                mid = (low + high) // 2 
                if po[mid] * s >= su:
                    temp = mid
                    high = mid - 1
                else:
                    low = mid + 1
            ans.append(m - temp)
        return ans