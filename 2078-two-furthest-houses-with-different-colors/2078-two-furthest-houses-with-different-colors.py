class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        mx = 0
        n = len(colors)
        for i in range(0,n-1):
            temp = 0
            for j in range(n-1, i, -1):
                if colors[i] != colors[j]:
                    temp = j - i
                    break
            mx = max(mx, temp)
        return mx    

        