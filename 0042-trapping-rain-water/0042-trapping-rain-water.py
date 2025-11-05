class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n
        temp = 0
        for i in range(n):
            if height[i] > temp:
                temp = height[i]
                maxL[i] = temp
            else:
                maxL[i] = temp 
        temp = 0
        for i in range(n-1, -1, -1):
            if height[i] > temp:
                temp = height[i]
                maxR[i] = temp
            else:
                maxR[i] = temp
        ans = [0] * n
        for i in range(n):
            ans[i] = min(maxL[i], maxR[i]) - height[i]
        summ = 0
        for i in range(n):
            summ += ans[i]
        return summ 