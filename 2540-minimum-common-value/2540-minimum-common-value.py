class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        def binarySearch(num, nums2):
            low = 0 
            high = m - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums2[mid] == num:
                    return True
                elif nums2[mid] > num:
                    high = mid - 1
                else:
                    low = mid + 1
            return False                
        for num in nums1:
            if binarySearch(num,nums2):
                return num
        return -1        