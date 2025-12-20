class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        res = set()
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1  
        return list(res)