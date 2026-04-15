class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        lt = []
        for i in range(n):
            if target == words[i]:
                lt.append(i)
        if not lt:
            return -1
        mn = 10 ** 9
        for ch in lt:
            t1 = abs(ch-startIndex)
            t3 = (n - ch) + startIndex
            t2 = (n - startIndex) + ch
            temp = min(t1, t2, t3)
            mn = min(mn, temp)
        return mn                 

          
