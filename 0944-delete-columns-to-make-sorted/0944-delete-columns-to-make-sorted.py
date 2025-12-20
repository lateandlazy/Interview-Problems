class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        m = len(strs)
        count = 0
        for i in range(n):
            for j in range(m-1):
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    count += 1
                    break
        return count            


