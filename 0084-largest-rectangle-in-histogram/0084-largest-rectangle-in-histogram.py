class Solution:
    def largestRectangleArea(self, hts: List[int]) -> int:
        n = len(hts)
        left = []
        st = []
        for i in range(n):
            if not st:
                left.append(-1)
            elif st and st[-1][0] < hts[i]:
                left.append(st[-1][1])
            elif st and st[-1][0] >= hts[i]:
                while st and st[-1][0] >= hts[i]:
                    st.pop()
                if not st:
                    left.append(-1)
                else:
                    left.append(st[-1][1])
            st.append((hts[i],i))
        right = []
        st = []
        for i in range(n-1, -1, -1):
            if not st:
                right.append(n)
            elif st and st[-1][0] < hts[i]:
                right.append(st[-1][1])
            elif st and st[-1][0] >= hts[i]:
                while st and st[-1][0] >= hts[i]:
                    st.pop()
                if not st:
                    right.append(n)
                else:
                    right.append(st[-1][1])
            st.append((hts[i],i))
        right.reverse()    
        ans = 0
        for i in range(n):
            w = right[i] - left[i] - 1
            ar = w * hts[i]
            ans = max(ans, ar)
        return ans 