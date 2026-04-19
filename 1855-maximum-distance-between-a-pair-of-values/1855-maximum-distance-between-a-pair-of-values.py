class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        def binaryS(y):
            low = 0
            high = m - 1
            ans = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums2[mid] < y:
                    high = mid - 1
                else:
                    low = mid + 1
                    ans = mid
            return ans
        mx = 0
        for i in range(n):
            x = binaryS(nums1[i])
            if x >= i:
                mx = max(mx, x - i)
        return mx    